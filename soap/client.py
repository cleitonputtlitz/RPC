from suds.client import Client
import time
import array as arr
from suds.sudsobject import Object


#lista = np.array([2147483647, 2147483647])
results = []
results.append('2147483647')
results.append('2147483647')
results.append('2147483647')
results.append('2147483647')
results.append('2147483647')
results.append('2147483647')

start_time = time.perf_counter()
i = 0

for n in range(5):
    
    start = time.perf_counter()
        
    #resp = server.exec(lista)

    
    hello_client = Client('http://localhost:8000/?wsdl')

    #pega o tipo do campo que esta no ?wsdl e seta o valor
    entry1 = hello_client.factory.create('stringArray')
    entry1.string = results
    print(entry1)

    #resp = hello_client.service.say_hello("Dave", 5)
    resp = hello_client.service.return_hello(entry1)
    print(type(resp))
    print(resp)

        
    end = time.perf_counter() - start   #latencia
        
    time_diff = time.perf_counter() - start_time
    i += 1

    print('{:.6f}s time for te execution '.format(end))
    print('{:.6f}s throughput for the execution '.format(i / time_diff))

    

