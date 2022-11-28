from tkinter import *
import random

# variables globales
BASE = 460
ALTURA = 380

# ventana principal
ventana_principal = Tk()
ventana_principal.title("Graficas 2D - Texto")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="green")

# frame de graficación
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=400)
frame_graficacion.pack(fill=BOTH, padx=10, pady=10)

# creación canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

# cuadrados y rectangulos
rect1 = c.create_rectangle(10, 10, BASE/2-10, ALTURA/2-10, fill="pink", outline="red")
rect2 = c.create_rectangle(10, 10, 110, 110, fill="green")
ventana_principal.mainloop()
