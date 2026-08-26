import tkinter as tk

def saludar():
    etiqueta.config(text="Ejemplo de boton", fg="blue")

ventana = tk.Tk()
ventana.title("Mi Primera Interfaz")
ventana.geometry("350x200")

etiqueta = tk.Label(ventana, text="Bienvenido a tu aplicación", font=("Arial", 14))
etiqueta.pack(pady=30) 

boton = tk.Button(ventana, text="Haz clic aquí", command=saludar)
boton.pack()

ventana.mainloop()