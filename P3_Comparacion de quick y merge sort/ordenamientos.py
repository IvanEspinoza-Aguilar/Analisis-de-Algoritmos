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

def exchangeSort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def quickSort(lista):
    arr = lista.copy()
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quickSort(left) + middle + quickSort(right)
    
def mergeSort(lista):
    arr = lista.copy()
    if len(arr) > 1:
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]
        
        leftHalf = mergeSort(leftHalf)
        rightHalf = mergeSort(rightHalf)
        
        merge(arr, leftHalf, rightHalf)
        
    return arr

def merge(arr, leftHalf, rightHalf):
    i = j = k = 0
    
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <rightHalf[j]:
            arr[k] = leftHalf[i]
            i += 1
        else:
            arr[k] = rightHalf[j]
            j += 1
        k += 1
    
    while i < len(leftHalf):
        arr[k] = leftHalf[i]
        i += 1
        k += 1
    
    while j < len(rightHalf):
        arr[k] = rightHalf[j]
        j += 1
        k += 1