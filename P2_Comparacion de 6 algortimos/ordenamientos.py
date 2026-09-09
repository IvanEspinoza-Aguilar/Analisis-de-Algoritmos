def bubbleSort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selectionSort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertionSort(lista):
    arr = lista.copy()
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

def gnomeSort(lista):
    arr = lista.copy()
    i = 0
    n = len(arr) 
    while i < n:
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1          
    return arr

def stoogeSortRec(arr, l, h):
    if l >= h:
        return
    # Si el primer elemento es mayor que el último, intercambiar
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
    # Si hay 3 o más elementos en el rango
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        # Aplicar fuerza bruta a los 3 tercios superpuestos
        stoogeSortRec(arr, l, h - t)       # Primeros 2/3
        stoogeSortRec(arr, l + t, h)       # Últimos 2/3
        stoogeSortRec(arr, l, h - t)       # Primeros 2/3 de nuevo

def stoogeSort(lista):
    arr = lista.copy()
    stoogeSortRec(arr, 0, len(arr) - 1)
    return arr

def exchangeSort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr