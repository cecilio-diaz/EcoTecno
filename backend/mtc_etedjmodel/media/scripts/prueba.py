import numpy as np

def prueba():
    for i in range(0,100,1):
#        A =B
        variable_rand = np.random.rand(1)
        print variable_rand
        f = open ('archivo_test_prueba.txt','w')
        f.write('hola mundo')
        f.close()
        
        
    return variable_rand


variable_rand = prueba()