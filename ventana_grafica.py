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
    main.pack_forget()
    global canvas_actual
    
    if canvas_actual:
        canvas_actual.get_tk_widget().destroy()
        
    figura = Figure(figsize=(9, 6), dpi=100)
    plano = figura.add_subplot(111)
    plano.plot(rango_x, rango_y, marker='o', color='red')
    #plano.plot(rango_x2, rango_y2, market='0', color='blue')
    
    plano.legend(['Bubble sort'])
    
    plano.set_title("Big O de el algoritmo de ordenamiento burbuja")
    plano.set_xlabel("Tamaño de n")
    plano.set_ylabel("Tiempo que tomado de cada ejecucion")

    canvas_actual = FigureCanvasTkAgg(figura, master=root)
    canvas_actual.draw()
    
    canvas_actual.get_tk_widget().pack(pady=10)

root = tk.Tk()
main = tk.Frame(root)
main.configure(bg="#ffffff")

root.configure(bg="#ffffff")
root.title("Vista de big O")
root.geometry("900x600")

lbl = tk.Label(root, text="Vista de big O graficado", fg="#ff0404")
lbl.configure(bg="#ffffff")
lbl.pack(pady=30)

tk.Label(main, text="Ingrese el tamaño inicial del arreglo:", bg="#ffffff", fg="#0408ff").pack(pady=5)
tamanio_inicial = tk.Entry(main)
tamanio_inicial.pack(pady=5)

tk.Label(main, text="Ingrese el incremento:", bg="#ffffff", fg="#0408ff").pack(pady=5)
incremento = tk.Entry(main)
incremento.pack(pady=5)

tk.Label(main, text="Ingrese el tamaño final del arreglo:", bg="#ffffff", fg="#0408ff").pack(pady=5)
tamanio_final = tk.Entry(main)
tamanio_final.pack(pady=5)

btn = tk.Button(main, text="Enviar datos a generar", command=pregunta_tamanio)
btn.pack(pady=10)

main.pack(pady=20)
root.mainloop()