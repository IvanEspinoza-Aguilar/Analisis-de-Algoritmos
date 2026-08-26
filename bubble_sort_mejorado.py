import time
from generador_arreglos import generador_arreglo

def pregunta_tamanio():
    tamanio_inicial = int(input("Dime el tamaño del arreglo: "))
    incremento = int(input("Dime el incremento de tamaño para los arreglos: "))
    tamanio_final = int(input("Dime el limite de tamaño para los arreglos: "))
    
    return tamanio_inicial, incremento, tamanio_final
    

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

tamanio_actual, incremento, tamanio_final = pregunta_tamanio()


while(tamanio_actual <= tamanio_final):
    arreglo_desordenado = generador_arreglo(tamanio_actual)
    tiempo_inicio = time.time()
    bubble_sort(arreglo_desordenado)
    tiempo_fin = time.time()
    
    tiempo_total = tiempo_fin - tiempo_inicio

    print("\n")
    #print("Lista ordenada:", arreglo_desordenado ,"\n")
    print("Tamanio del arreglo que se esta ordenando: ", tamanio_actual)
    print(f"Tiempo total en ordenar: {tiempo_total:.6f}")
    
    print("-------------------------------------------------")
    tamanio_actual = tamanio_actual + incremento