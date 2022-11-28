from tkinter import Tk, Canvas, Scale

ancho = 400
alto = 200
radio = 75

def gira_circulo(angulo):
    angulo2 = int(angulo)+120
    angulo3 = int(angulo)+240
    canvas.itemconfig(arco1, start=angulo)
    canvas.itemconfig(arco2, start=angulo2)
    canvas.itemconfig(arco3, start=angulo3)
    
root = Tk()
root.title("Arco")
root.resizable(False, False)

canvas = Canvas(width=ancho, height=alto)

arco1 = canvas.create_arc(ancho/2-radio, alto/2-radio, ancho/2+radio, alto/2+radio, start=120, extent=45, fill="blue", outline="")

arco2 = canvas.create_arc(ancho/2-radio, alto/2-radio, ancho/2+radio, alto/2+radio, start=240, extent=45, fill="blue", outline="")

arco3 = canvas.create_arc(ancho/2-radio, alto/2-radio, ancho/2+radio, alto/2+radio, start=360, extent=45, fill="blue", outline="")

barra_deslizamiento = Scale(from_=0, to=360, orient="horizontal", length=ancho, command=gira_circulo, tickinterval=90)

canvas.pack()
barra_deslizamiento.pack()

root.mainloop()
