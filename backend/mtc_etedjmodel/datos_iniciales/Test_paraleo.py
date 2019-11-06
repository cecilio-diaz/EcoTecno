# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 14:14:03 2018

@author: Cecilio-Diaz
"""

#from time import time
#def fibonacci(n):
#    if n < 2: return n
#    return fibonacci(n-1) + fibonacci(n-2)
#
#start = time()
#for i in range(30, 35):
#    fibonacci(i)
#
#print('Tardó {} segundos.'.format(time() - start))

## Tardó 3.23 segundos
#Tardó 5.42499995232 segundos.
#Tardó 4.85399985313 segundos.
#Tardó 4.79400014877 segundos.


#from threading import Thread
#threads = []
#start = time()
#for i in range(30, 35):
#    t = Thread(target=fibonacci, args=(i,))
#    t.start()
#    threads.append(t)
#
#for t in threads: t.join() # Esperamos a que terminen
#print('Tardó {} segundos.'.format(time() - start))

#Tardó 22.378000021 segundos.
#Tardó 23.1449999809 segundos.


class Counter(object):
    def __init__(self):
        self.count = 0
    
    def increment(self, n):
        self.count += n

def count_up(counter, how_many):
    for i in range(how_many):
        counter.increment(1)

threads = []
args = (Counter(), 1000)
for i in range(20):
    t = Thread(target=count_up, args=args)
    t.start()
    threads.append(t)

for t in threads: t.join()
print('Counter: {}.'.format(args[0].count))