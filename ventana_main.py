import tkinter as tk
from tkinter import messagebox
from proceso import Proceso

procesosCapturados = []
idRegistrados = []

def Verificacion():
    nombreTemp = nombreProgramador.get()
    operacionTemp = operacion.get()
    
    if not nombreTemp or not operacionTemp:
        messagebox.showwarning("Error", "El nombre y la operación no pueden estar vacíos.")
        return
    
    operadoresValidos = ['+', '-', '*', '/', '%']
    operadorEncontrado = None

    for op in operadoresValidos:
        if op in operacionTemp:
            operadorEncontrado = op
            break

    if not operadorEncontrado:
        messagebox.showerror("Error", "Operación no válida. Usa +, -, *, / o %")
        return

    try:
        partes = operacionTemp.split(operadorEncontrado)
        
        if len(partes) != 2:
            raise ValueError
            
        numero1 = float(partes[0])
        numero2 = float(partes[1])
        
        if operadorEncontrado in ['/', '%'] and numero2 == 0:
            messagebox.showerror("Error Matemático", "¡No se puede dividir entre cero!")
            operacion.focus()
            return
            
    except ValueError:
        messagebox.showerror("Error", "La operación debe tener dos números válidos.")
        return
    
    try:
        tiempoMaximo = int(TME.get())
        idPrograma = int(numeroProgra.get())
        
        nuevoProceso = Proceso(nombreTemp, operacionTemp, tiempoMaximo, idPrograma)
        
        procesosCapturados.append(nuevoProceso)
        idRegistrados.append(idPrograma)
        
        messagebox.showinfo("Éxito", f"Proceso {idPrograma} guardado correctamente.\nTotal procesos: {len(procesosCapturados)}")
        
        nombreProgramador.delete(0, tk.END)
        operacion.delete(0, tk.END)
        TME.delete(0, tk.END)
        numeroProgra.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "El Tiempo Máximo y el Número de Programa deben ser números enteros.")
    
def EnviarDatos():
    listaLotes = []
    loteTemp = []
    
    for i in procesosCapturados:
        loteTemp.append(i)
        if(len(loteTemp) == 5):
            listaLotes.append(loteTemp)
            loteTemp = []
            
    if len(loteTemp) > 0:
        listaLotes.append(loteTemp)
        
    print(f"Se crearon {len(listaLotes)} lotes en total.")
        
root = tk.Tk()
main = tk.Frame(root)
main.configure(bg="#ffffff")

root.configure(bg="#ffffff")
root.title("Simulacion de proceso por lotes")
root.geometry("900x600")

lbl = tk.Label(root, text="Procesamiento por lotes", fg="#ff0404", font=("Arial", 20, "bold"))
lbl.configure(bg="#ffffff")
lbl.pack(pady=30)

tk.Label(main, text="Nombre del programador:", bg="#ffffff", fg="#0408ff", font=("Arial", 16)).pack(pady=5)
nombreProgramador = tk.Entry(main)
nombreProgramador.pack(pady=5)

tk.Label(main, text="Operacion a realizar", bg="#ffffff", fg="#0408ff", font=("Arial", 16)).pack(pady=5)
operacion = tk.Entry(main)
operacion.pack(pady=5)

tk.Label(main, text="Tiempo maximo estimado", bg="#ffffff", fg="#0408ff", font=("Arial", 16)).pack(pady=5)
TME = tk.Entry(main)
TME.pack(pady=5)

tk.Label(main, text="Numero de programa", bg="#ffffff", fg="#0408ff", font=("Arial", 16)).pack(pady=5)
numeroProgra = tk.Entry(main)
numeroProgra.pack(pady=5)

btn = tk.Button(main, text="Enviar datos a verificar", command=Verificacion, font=("Arial", 12))
btn.pack(pady=20)

btn = tk.Button(main, text="Iniciar simulacion", command=EnviarDatos, font=("Arial", 12))
btn.pack(pady=20)

main.pack(pady=20)
root.mainloop()