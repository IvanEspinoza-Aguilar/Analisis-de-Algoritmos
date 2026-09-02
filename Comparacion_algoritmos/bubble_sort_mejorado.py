import time
from Comparacion_algoritmos.generador_arreglos import generador_arreglo

def bubble_sort_brute_force(arr):
    n = len(arr)
    # Ciclo externo corre n veces de forma fija
    for i in range(n):
        # Ciclo interno compara elementos adyacentes
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                # Intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def inicio_pruebas(tamanio_actual, incremento, tamanio_final):
    tamanio_valores_arreglos = []
    tiempo_registrado = []
    
    while(tamanio_actual <= tamanio_final):
        
        arreglo_desordenado = generador_arreglo(tamanio_actual)
        tiempo_inicio = time.time()
        bubble_sort_brute_force(arreglo_desordenado)
        tiempo_fin = time.time()
        
        tiempo_total = tiempo_fin - tiempo_inicio
        
        tamanio_valores_arreglos.append(tamanio_actual)
        tiempo_registrado.append(tiempo_total)
        
        tamanio_actual = tamanio_actual + incremento
        
    return tamanio_valores_arreglos, tiempo_registrado
