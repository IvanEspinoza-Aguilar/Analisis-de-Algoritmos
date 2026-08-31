import time
from generador_arreglos import generador_arreglo

def bubble_sort(arr):
    #Complejidad temporal
    #print(type(arr))
    print(len(arr))

    #time.sleep(100)

    n = len(arr)

    #Bucle exterior:
    for i in range(n): #0(0)
        #Bucle interior:
        for j in range(0, n-i-1):
            #Comparacion: 0(1)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #0(1)

def inicio_pruebas(tamanio_actual, incremento, tamanio_final):
    tamanio_valores_arreglos = []
    tiempo_registrado = []
    
    while(tamanio_actual <= tamanio_final):
        
        arreglo_desordenado = generador_arreglo(tamanio_actual)
        tiempo_inicio = time.time()
        bubble_sort(arreglo_desordenado)
        tiempo_fin = time.time()
        
        tiempo_total = tiempo_fin - tiempo_inicio
        
        tamanio_valores_arreglos.append(tamanio_actual)
        tiempo_registrado.append(tiempo_total)
        
        tamanio_actual = tamanio_actual + incremento
        
    return tiempo_registrado, tamanio_valores_arreglos
