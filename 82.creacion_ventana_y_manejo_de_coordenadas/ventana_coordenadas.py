from tkinter import *
# -----------------
# Ventana principal
# -----------------

ventana_principal = Tk()
# Título de la ventana
ventana_principal.title("Sistemas UIS")

# Tamaño de la ventana
ventana_principal.geometry("500x500")
# Deshabilitar botón de maximixar
ventana_principal.resizable(0,0)

# Color de fondo de la ventana
ventana_principal.config(bg="black")

# -------------------
# frame entrada datos
# -------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="gray", width=480, height=240)
frame_entrada.place(x=10, y=10)

# Logo de la App

logo = PhotoImage(file="img/logo_uis.png")
lb_logo = Label(frame_entrada, image=logo)
lb_logo.place(x=10, y=10)

ventana_principal.mainloop()
