from tkinter import *

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
c.place(x=10, y=10)

# lineas
linea1 = c.create_line(0, 0, BASE, ALTURA, fill="red")
linea2 = c.create_line(0, ALTURA, BASE, 0, fill="red")
linea3 = c.create_line(BASE/2, 0, BASE/2, ALTURA, fill="green")
linea4 = c.create_line(0, ALTURA/2, BASE, ALTURA/2, fill="green")

# desplegar ventana principal. Queda a la espera de eventos
ventana_principal.mainloop()
