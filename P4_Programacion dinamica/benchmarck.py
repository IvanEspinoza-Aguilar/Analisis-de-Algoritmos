import time
from fibonacci import fibonacci
from fibonacci_recursivo import fibonacci_dp

def inicioDePruebas(inicio, incremento, fin, seleccion):
    
    fibonacciSeleccionado = {
        "Fibonacci" : fibonacci,
        "Fibonacci DP" : fibonacci_dp
    }
    
    if seleccion == "Ambos fibonacci":
        ejecutar = fibonacciSeleccionado
    else:
        ejecutar = {seleccion: fibonacciSeleccionado[seleccion]}
            
    tamanios = []
    tiempos = {nombre: [] for nombre in ejecutar}
    
    for i in range(inicio, fin+1, incremento):
        tamanios.append(i)
        
    for n in tamanios:
        for nombre, funcion in ejecutar.items():
            t_ini = time.time()
            funcion(n)
            t_fin = time.time()
            tiempos[nombre].append(t_fin - t_ini)
        
    return tamanios, tiempos