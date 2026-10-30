import heapq
from collections import defaultdict

class Nodo:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.izq = None
        self.der = None
        
    def __lt__(self, otro):
        return self.freq < otro.freq
        
def construirArbol(freqs):
    heap = [Nodo(c, f) for c, f in freqs.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        izq = heapq.heappop(heap)
        der = heapq.heappop(heap)
        nodo = Nodo(None, izq.freq + der.freq)
        nodo.izq, nodo.der = izq, der
        heapq.heappush(heap, nodo)
    
    return heap[0]

def generarCodigos(nodo, prefijos="", codigos={}):
    if nodo is None:
        return
    if nodo.char is not None:
        codigos[nodo.char] = prefijos
    
    generarCodigos(nodo.izq, prefijos + "0", codigos)
    generarCodigos(nodo.der, prefijos + "1", codigos)
    
    return codigos

texto = "Compresor de arhivos de texto con el algoritmo de Huffman"

freqs = defaultdict(int)
for c in texto:
    freqs[c] +=1
    
raiz = construirArbol(freqs)
codigos = generarCodigos(raiz)

codificado = "".join(codigos[c] for c in texto)

print("Codigos de Huffman: " , codigos)
print("Texto original:", texto)
print("Codificado", codificado)