import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from benchmarck import inicioPruebas

canvaActual = None

def preguntarDatos():
    seleccion = caja.get()
    inicio = int(tamanioInicial.get())
    incrementoArr = int(incremento.get())
    final = int(tamanioFinal.get())
    
    tamanios, tiempos = inicioPruebas(inicio, incrementoArr, final, seleccion)
    generarGrafica(tamanios, tiempos)

def generarGrafica(x, y):
    main.pack_forget()
    global canvaActual
    
    if canvaActual:
        canvaActual.get_tk_widget().destroy()
        
    figura = Figure(figsize=(9, 6), dpi=100)
    
    if "Stooge sort" in y and len(y) > 1:
        plano1 = figura.add_subplot(211)
        for nombre, tiempo in y.items():
            if nombre != "Stooge sort":
                plano1.plot(x, tiempo, marker="o", label=nombre)
        plano1.grid()
        plano1.legend()
        plano1.set_title("Algoritmos Rápidos e Intermedios")
        plano1.set_ylabel("Tiempo (s)")
        
        plano2 = figura.add_subplot(212)
        plano2.plot(x, y["Stooge sort"], marker="o", color="purple", label="Stooge sort")
        plano2.grid()
        plano2.legend()
        plano2.set_title("Stooge Sort (Escala de tiempo mayor)")
        plano2.set_xlabel("Tamaño de n")
        plano2.set_ylabel("Tiempo (s)")
        
        figura.tight_layout()
    else:
        plano = figura.add_subplot(111)
        for nombre, tiempo in y.items():
            plano.plot(x, tiempo, marker="o", label=nombre)
        plano.grid()
        plano.legend()
        plano.set_title("Big O del algoritmo")
        plano.set_xlabel("Tamaño de n")
        plano.set_ylabel("Tiempo (s)")

    canvaActual = FigureCanvasTkAgg(figura, master=root)
    canvaActual.draw()
    canvaActual.get_tk_widget().pack(pady=10)
    
root = tk.Tk()
root.configure(bg="#ffffff")
root.title("Graficacion de algoritmos")
root.geometry("900x600")

main = tk.Frame(root)
main.configure(bg="#ffffff")

lbl = tk.Label(root, text="Vista de nuevos algoritmos a analizar", fg="#CE0606", font=("Arial", 20 , "bold"))
lbl.configure(bg="#ffffff")
lbl.pack(pady=30)

opciones = ["Bubble sort", "Selection sort", "Insertion sort", "Gnome sort", "Exchange sort", "Stooge sort", "Todos los algoritmos"]

caja = ttk.Combobox(main, values=opciones, state="readonly")
caja.current(0)
caja.pack(pady=20)

tk.Label(main, text="Ingrese el tamaño inicial del arreglo:", bg="#ffffff", fg="#0408ff", font=("Arial", 12)).pack(pady=5)
tamanioInicial = tk.Entry(main)
tamanioInicial.pack(pady=5)

tk.Label(main, text="Ingrese el incremento del arreglo:", bg="#ffffff", fg="#0408ff", font=("Arial", 12)).pack(pady=5)
incremento = tk.Entry(main)
incremento.pack(pady=5)

tk.Label(main, text="Ingrese el tamaño final del arreglo:", bg="#ffffff", fg="#0408ff", font=("Arial", 12)).pack(pady=5)
tamanioFinal = tk.Entry(main)
tamanioFinal.pack(pady=5)

boton = tk.Button(main, text="Enviar los datos a generar", command=preguntarDatos)
boton.pack(pady=10)

main.pack(pady=20)
root.mainloop()