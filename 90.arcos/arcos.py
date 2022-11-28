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
arc1 = c.create_arc(10, 10, 210, 210, start=45, extent=90, fill="red")
    
# desplegar ventana principal. Queda a la espera de eventos
ventana_principal.mainloop()
