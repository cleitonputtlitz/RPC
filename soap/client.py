from weakref import proxy
from suds.client import Client
import time

param = []
for i in range(10000):
    param.append(2147483647)

# w sobrescreve; a adiciona no final
f = open("log.csv", "a")
#f.write("latencia; throughput\n")

start_time = time.perf_counter()
i = 0

proxy = Client('http://143.54.49.122:8000/?wsdl')

for n in range(100):
    
    start = time.perf_counter()   

    print("Enviando req ", n)

    #pega o tipo do campo que esta no ?wsdl e seta o valor
    entry1 = proxy.factory.create('stringArray')
    entry1.string = param
    #print(entry1)

    #resp = proxy.service.say_hello("Dave", 5)
    resp = proxy.service.return_hello(entry1)
        
    end = time.perf_counter() - start   #latencia
        
    time_diff = time.perf_counter() - start_time
    i += 1


    #print('{:.6f}s time for te execution '.format(end))
    #print('{:.6f}s throughput for the execution '.format(i / time_diff))

    f.write(str(i) + "; " + str("{:.6f}".format(end)) + "; " + str("{:.6f}".format(i / time_diff))+";\n")
     
f.close()

    

