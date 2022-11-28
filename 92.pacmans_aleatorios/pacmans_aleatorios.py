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

# arcos
for i in range(100):

    color = "#"
    for j in range(6):
        color = color + random.choice("0123456789ABCDEF")

    x = random.randint(0, BASE-20)
    y = random.randint(0, ALTURA-20)
    arc1 = c.create_arc(x, y, x+20, y+20, start=45, extent=270, fill=color)
    elip1 = c.create_oval(x+5, y+5, x+8, y+8, fill="black")
    
# desplegar ventana principal. Queda a la espera de eventos
ventana_principal.mainloop()
