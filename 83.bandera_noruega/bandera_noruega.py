from tkinter import *

ventana = Tk()
ventana.title("Bandera de Noruega")
ventana.geometry("750x500")
ventana.resizable(0, 0)
ventana.config(bg="white")

# cuadros rojos
frame_cr1 = Frame(ventana)
frame_cr1.config(bg="red", width=200, height=200)
frame_cr1.place(x=10, y=10)

frame_cr2 = Frame(ventana)
frame_cr2.config(bg="red", width=200, height=200)
frame_cr2.place(x=10, y=290)

frame_cr3 = Frame(ventana)
frame_cr3.config(bg="red", width=450, height=200)
frame_cr3.place(x=290, y=10)

frame_cr4 = Frame(ventana)
frame_cr4.config(bg="red", width=450, height=200)
frame_cr4.place(x=290, y=290)

# cuadros azules
frame_ca1 = Frame(ventana)
frame_ca1.config(bg="blue", width=730, height=40)
frame_ca1.place(x=10, y=230)

frame_ca2 = Frame(ventana)
frame_ca2.config(bg="blue", width=40, height=480)
frame_ca2.place(x=230, y=10)

ventana.mainloop()
