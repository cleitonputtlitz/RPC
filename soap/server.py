from multiprocessing.dummy import Array
from typing import List, Sequence
from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, String

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param name the name to say hello to
        @param times the number of times to say hello
        @return the completed array
        """

        for i in range(times):
            yield u'Hello, %s' % name

class returnReceive(ServiceBase):
    #List(min_occurs=1, max_occurs='unbounded', nillable=False)
    @rpc(Iterable(Unicode), _returns=Iterable(Unicode))
    def return_hello(ctx, parm):
        return parm

application = Application([HelloWorldService, returnReceive], 'spyne.examples.hello.soap',
                in_protocol=Soap11(),
                out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()