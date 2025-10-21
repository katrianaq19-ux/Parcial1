import tkinter as tk
from tkinter import ttk

class Orden:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.insert(0, item)

    def mostrar(self):
        return self.items

# Orden alfabético personalizado
Lista1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","T","U"]

# Función para ordenar según Lista1
def ordenar_personalizado(lista):
    return sorted(lista, key=lambda x: Lista1.index(x.upper()))


def interfaz():
    root = tk.Tk()
    root.title("Ordenador de Letras Personalizado")
    root.geometry("450x350")

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(frame, text= "Ingrese letras separadas por comas (ej: l,u,i,s,a):").pack(pady=5)
    entrada = ttk.Entry(frame, width=40)
    entrada.pack(pady=5)

    ttk.Label(frame, text="Lista original:").pack()
    original_label = ttk.Label(frame, text="")
    original_label.pack()

    ttk.Label(frame, text="Lista ordenada:").pack()
    ordenada_label = ttk.Label(frame, text="")
    ordenada_label.pack()

    def ordenar_y_mostrar():
        texto = entrada.get()
        letras = [x.strip().upper() for x in texto.split(",") if x.strip()]
        original_label.config(text=", ".join(letras))
        ordenada = ordenar_personalizado(letras)
        ordenada_label.config(text=", ".join(ordenada))

    ordenar_btn = ttk.Button(frame, text="Ordenar", command=ordenar_y_mostrar)
    ordenar_btn.pack(pady=10)

    root.mainloop()

interfaz()