import random

def generadorArreglo(n, min_val, max_val):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(min_val, max_val))
    return arreglo