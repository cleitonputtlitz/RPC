from multiprocessing.dummy import Array
from typing import List, Sequence
from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, String

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import psutil
import time

#143.54.49.122
global last_time
last_time = 0

def CPU_Memory_Usage():
    global last_time
    if(time.time() - last_time >= 1):
        last_time = time.time()
        #Obtém informações de uso da CPU
        cpu_percent = psutil.cpu_percent()
        # Obtém informações de uso da memória
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        f.write(str("{:.6f}".format(cpu_percent)) + "; " + str("{:.6f}".format(memory_percent))+";\n")


class returnReceive(ServiceBase):
    #List(min_occurs=1, max_occurs='unbounded', nillable=False)
    @rpc(Iterable(Unicode), _returns=Iterable(Unicode))
    def return_hello(ctx, parm):
        CPU_Memory_Usage()
        x = parm
        return x

application = Application([returnReceive], 'spyne.examples.hello.soap',
                in_protocol=Soap11(),
                out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    
    from wsgiref.simple_server import make_server

    print("listening  on port 8000")
    f = open("log_server.csv", "a")
    f.write("cpu; memoria;\n")

    server = make_server('0.0.0.0', 8000, wsgi_application)
    server.serve_forever()
    
    f.close()
