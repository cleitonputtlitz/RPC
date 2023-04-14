import xmlrpc.client
import time
import psutil
import os

#with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
with xmlrpc.client.ServerProxy("http://143.54.49.122:8000/") as proxy:

    param = []
    for i in range(100):
        param.append(2147483647)
   
    
    start_time = time.perf_counter()
    i = 0
    
    f = open("log.csv", "a")
    #f.write("latencia; throughput\n")

    for n in range(100):
                
        start = time.perf_counter()
        
        print("Enviando req ", n)
        
        resp = proxy.exec(param)
        
        end = time.perf_counter() - start   #latencia
        
        time_diff = time.perf_counter() - start_time
        i += 1               
                        
        #print('{:.6f}s time for te execution '.format(end))
        #print('{:.6f}s throughput for the execution '.format(i / time_diff))

        #print(psutil.cpu_percent())
        #print(psutil.cpu_count())

         
        #print('RAM memory % used:', psutil.virtual_memory()[2]) 
    
        #tempo ; latencia ; throughput
        f.write(str(i) + "; " + str("{:.6f}".format(end)) + "; " + str("{:.6f}".format(i / time_diff))+";\n")
    
        
        #print("retorno " + str(len(lista)) + " len ret " + str(len(resp)) + " " +  str(time_env) + " " + str(time_rec) + " tempo: " + str(tempo))
        
    f.close()
        
        
#  Casos de teste
#   - mensagens pequenas    = 1 parametros
#   - mensagens grandes     = 2016 parametros
#
#   - poucos usuarios       = 1 usuarios
#   - muitos usuarios       = 100 usuarios
#
#   AVALIAR
#   - tempo de resposta da API
#   90 percentil (ordenar os dados e pegar os 90% do meio)
#   - Throughput 
#   dados por segundo        
#   Contar as requisições finalizadas e dividir pelo tempo que o programa já levou para executar?
#
#   enviar uma nova requisicao a cada x tempo
