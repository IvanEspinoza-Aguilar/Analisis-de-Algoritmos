import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from benchmarck import inicioDePruebas

canvaActual = None

def preguntarDatos():
    seleccion = caja.get()
    inicio = int(tamanioInicial.get())
    incrementoArr = int(incremento.get())
    final = int(tamanioFinal.get())
    
    tamanios, tiempos = inicioDePruebas(inicio, incrementoArr, final, seleccion)
    generarGrafica(tamanios, tiempos)

def generarGrafica(x, y):
    main.pack_forget()
    global canvaActual
    
    if canvaActual:
        canvaActual.get_tk_widget().destroy()
        
    figura = Figure(figsize=(9, 6), dpi=100)
    
    plano = figura.add_subplot(111)
    for nombre, tiempo in y.items():
        plano.plot(x, tiempo, marker="o", label=nombre)
    plano.grid()
    plano.legend()
    plano.set_title("Big O de fibonacci")
    plano.set_xlabel("Tamaño de n")
    plano.set_ylabel("Tiempo (s)")

    canvaActual = FigureCanvasTkAgg(figura, master=root)
    canvaActual.draw()
    canvaActual.get_tk_widget().pack(pady=10)
    
root = tk.Tk()
root.configure(bg="#ffffff")
root.title("Graficacion de fibonacci")
root.geometry("900x600")

main = tk.Frame(root)
main.configure(bg="#ffffff")

lbl = tk.Label(root, text="Vista de fibonacci sin programacion dinamica y con programacion dinamica", fg="#CE0606", font=("Arial", 16 , "bold"))
lbl.configure(bg="#ffffff")
lbl.pack(pady=30)

opciones = ["Fibonacci", "Fibonacci DP", "Ambos fibonacci"]

caja = ttk.Combobox(main, values=opciones, state="readonly")
caja.current(0)
caja.pack(pady=20)

tk.Label(main, text="Ingrese el tamaño inicial de fibonacci:", bg="#ffffff", fg="#0408ff", font=("Arial", 12)).pack(pady=5)
tamanioInicial = tk.Entry(main)
tamanioInicial.pack(pady=5)

tk.Label(main, text="Ingrese el incremento de fibonacci:", bg="#ffffff", fg="#0408ff", font=("Arial", 12)).pack(pady=5)
incremento = tk.Entry(main)
incremento.pack(pady=5)

tk.Label(main, text="Ingrese el tamaño final de fibonacci:", bg="#ffffff", fg="#0408ff", font=("Arial", 12)).pack(pady=5)
tamanioFinal = tk.Entry(main)
tamanioFinal.pack(pady=5)

boton = tk.Button(main, text="Enviar los datos a generar", command=preguntarDatos)
boton.pack(pady=10)

main.pack(pady=20)
root.mainloop()