import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from bubble_sort_mejorado import inicio_pruebas

canvas_actual = None

def pregunta_tamanio():
    valor_arreglo = int(tamanio_inicial.get())
    valor_incremento = int(incremento.get())
    valor_arreglo_final = int(tamanio_final.get())
    
    datos_x, datos_y = inicio_pruebas(valor_arreglo, valor_incremento, valor_arreglo_final)
    generar_grafica(datos_x, datos_y)
    
def generar_grafica(rango_x, rango_y):
    global canvas_actual
    
    if canvas_actual:
        canvas_actual.get_tk_widget().destroy()
        
    figura = Figure(figsize=(6, 4), dpi=100)
    plano = figura.add_subplot(111)
    plano.plot(rango_x, rango_y, marker='o', color='red')
    
    plano.set_title("Big O de el algoritmo de ordenamiento burbuja")
    plano.set_xlabel("Tiempo de ejecucion")
    plano.set_ylabel("Elementos del arreglo")

    canvas = FigureCanvasTkAgg(figura, master=root)
    canvas.draw()
    
    canvas.get_tk_widget().pack(pady=10)

root = tk.Tk()
root.title("Vista de big O")
root.geometry("900x600")

lbl = tk.Label(root, text="Vista de big O \n para el algoritmo \n de ordenamiento burbuja graficado")
lbl.pack(pady=30)

tk.Label(root, text="Ingrese el tamaño inicial del arreglo:").pack(pady=5)
tamanio_inicial = tk.Entry(root)
tamanio_inicial.pack(pady=5)

tk.Label(root, text="Ingrese el incremento:").pack(pady=5)
incremento = tk.Entry(root)
incremento.pack(pady=5)

tk.Label(root, text="Ingrese el tamaño final del arreglo:").pack(pady=5)
tamanio_final = tk.Entry(root)
tamanio_final.pack(pady=5)

btn = tk.Button(root, text="Enviar datos a generar", command=pregunta_tamanio)
btn.pack(pady=10)

root.mainloop()