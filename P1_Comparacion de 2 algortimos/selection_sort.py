import time
from generador_arreglos import generador_arreglo

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        # Buscamos en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el menor encontrado con el primer elemento actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def inicio_pruebas_sel(tamanio_actual, incremento, tamanio_final):
    tamanio_valores_arreglos = []
    tiempo_registrado = []
    
    while(tamanio_actual <= tamanio_final):
        
        arreglo_desordenado = generador_arreglo(tamanio_actual)
        tiempo_inicio = time.time()
        selection_sort(arreglo_desordenado)
        tiempo_fin = time.time()
        
        tiempo_total = tiempo_fin - tiempo_inicio
        
        tamanio_valores_arreglos.append(tamanio_actual)
        tiempo_registrado.append(tiempo_total)
        
        tamanio_actual = tamanio_actual + incremento
        
    return tiempo_registrado
