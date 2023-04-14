from xmlrpc.server import SimpleXMLRPCServer
import psutil
import time

global last_time
last_time = 0

def exec(n):
    print("Requisição recebida com tamanho: " + str(len(n)))
    x = n
    CPU_Memory_Usage()
    return x
    
def CPU_Memory_Usage():
    global last_time
    
    #print(time.localtime(time.time()))
    #print(time.localtime(last_time))
    #print(time.time() - last_time)
    
    if(time.time() - last_time >= 1):
        last_time = time.time()        
        #Obtém informações de uso da CPU
        cpu_percent = psutil.cpu_percent()
        # Obtém informações de uso da memória
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        f.write(str(time.localtime(time.time())) + "; " + str("{:.6f}".format(cpu_percent)) + "; " + str("{:.6f}".format(memory_percent))+";\n")


server = SimpleXMLRPCServer(("0.0.0.0", 8000))  #0.0.0.0 ao inves de localhost para funcionar entre diferentes maquinas

print("Listening on port 8000...")

f = open("log_server.csv", "a")
f.write("cpu; memoria;\n")
    
server.register_function(exec, "exec")
server.serve_forever()

f.close()
