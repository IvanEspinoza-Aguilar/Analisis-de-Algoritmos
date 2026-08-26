import tkinter as tk

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "Ivan Espinoza Aguilar"
    lbl.config(text=f"Hola , {nombre}")


root = tk.Tk()
root.title("Saludar Gente")
root.geometry("360x220")

#Crear Etiquetas
lbl = tk.Label(root, text="Hola, escribe tu nombre y apellido")
lbl.pack(pady=30)

#Entrada de texto
entrada = tk.Entry(root)
entrada.pack(pady=5)

#Creacion de boton
btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=10)

root.mainloop()