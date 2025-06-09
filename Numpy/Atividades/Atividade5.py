import numpy as np
def estatisticas_array(array):
    soma = np.sum(array)
    media = np.mean(array)
    return soma, media

o_array = np.array([80,50,30,20,10])
print(estatisticas_array(o_array))
    
        

