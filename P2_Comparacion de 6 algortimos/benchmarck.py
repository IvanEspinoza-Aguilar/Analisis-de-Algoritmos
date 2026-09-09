import time
from generadorArreglos import generadorArreglo
from ordenamientos import *

def inicioPruebas(inicio, incremento, fin, seleccion):
    
    algortimoSeleccionado = {
        "Bubble sort" : bubbleSort,
        "Selection sort" : selectionSort,
        "Insertion sort" : insertionSort,
        "Gnome sort" : gnomeSort,
        "Exchange sort" : exchangeSort,
        "Stooge sort" : stoogeSort
    }
    
    if seleccion == "Todos los algoritmos":
        ejecutar = algortimoSeleccionado
    else:
        ejecutar = {seleccion: algortimoSeleccionado[seleccion]}
            
    tamanios = []
    listas = []
    tiempos = {nombre: [] for nombre in ejecutar}
    
    for i in range(inicio,fin+1,incremento):
        listas.append(generadorArreglo(i,1,100))
        tamanios.append(i)
    
    for arreglo in listas:
        for nombre, funcion in ejecutar.items():
            t_ini = time.time()
            funcion(arreglo)
            t_fin = time.time()
            tiempos[nombre].append(t_fin - t_ini)
        
    return tamanios,  tiempos