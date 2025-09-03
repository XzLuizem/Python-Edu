### interfaz tkinter ###

import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

caja_texto = tkinter.Entry(ventana)
# caja_texto.pack()
caja_texto.grid(row=0, column=2)


def texto_de_la_caja():
    text_20 = caja_texto.get()
    # print("Texto de la caja: " + text_20)
    etiqueta["text"] = text_20


def saludo(nombre):
    print("Hola " + nombre)


etiqueta = tkinter.Label(
    ventana,
    text="Hola, mundo!",
    bg="blue",
    fg="white",
    font=("Arial", 24)
)
# etiqueta.pack(fill=tkinter.X, expand=True)
etiqueta.grid(row=2, column=1)

boton1 = tkinter.Button(
    ventana,
    text="botón 1",
    width=10,
    height=5,
    # padx=40,
    # pady=20,
    command=lambda: saludo("Python")
    # command=lambda: print("¡Botón clickeado!")
)
# boton1.pack()
boton1.grid(row=0, column=0)

boton2 = tkinter.Button(
    ventana,
    text="botón 2",
    width=10,
    height=5,
    command=texto_de_la_caja
)
boton2.grid(row=1, column=0)

boton3 = tkinter.Button(
    ventana,
    text="botón 3",
    width=10,
    height=5,
    command=texto_de_la_caja
)
boton3.grid(row=2, column=0)

ventana.mainloop()
