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

# texto
texto = c.create_text(BASE/2, ALTURA/2, anchor="center", text="UIS Socorro", font=("Arial", "30", "bold"), fill="blue", activefill="red")

# poligonos/triangulos
poli1 = c.create_polygon(0, ALTURA, BASE/2, 0, BASE, ALTURA, fill="green", outline="red", width=5)

# rombo
rombo = c.create_polygon(0, ALTURA/2, BASE/2, ALTURA, BASE, ALTURA/2, BASE/2, 0, fill="blue", outline="white", width=5)

# desplegar ventana principal. Queda a la espera de eventos
ventana_principal.mainloop()
