import random

def generador_arreglo(tamanio):
    
    arreglo = []
    
    for i in range(tamanio):
        arreglo.append(random.randint(-100, 100))
        
    return arreglo