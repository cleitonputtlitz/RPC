from xmlrpc.server import SimpleXMLRPCServer

def exec(n):
    print("Requisição recebida com tamanho: " + str(len(n)))
    return n

server = SimpleXMLRPCServer(("0.0.0.0", 8000))  #0.0.0.0 ao inves de localhost para funcionar entre diferentes maquinas
print("Listening on port 8000...")
server.register_function(exec, "exec")
server.serve_forever()