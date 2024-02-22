import re
from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

i = 0

#Entrada
e_texto = Entry(ventana, font=("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Funciones
def borrar_caracter():
    texto_actual = e_texto.get()
    nuevo_texto = texto_actual[:-1]
    e_texto.delete(0, END)
    e_texto.insert(0, nuevo_texto)

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar_todo():
    e_texto.delete(0, END)
    i = 0

def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

# Validación de entrada
def validar_entrada(entrada):
    patron = r'^[0-9+*./()-]*$'
    return re.match(patron, entrada) is not None

# Botones
def boton_numero(valor):
    if validar_entrada(valor):
        click_boton(valor)

boton0 = Button(ventana, text="0", width=5, height=2, command=lambda: boton_numero("0"))
boton1 = Button(ventana, text="1", width=5, height=2, command=lambda: boton_numero("1"))
boton2 = Button(ventana, text="2", width=5, height=2, command=lambda: boton_numero("2"))
boton3 = Button(ventana, text="3", width=5, height=2, command=lambda: boton_numero("3"))
boton4 = Button(ventana, text="4", width=5, height=2, command=lambda: boton_numero("4"))
boton5 = Button(ventana, text="5", width=5, height=2, command=lambda: boton_numero("5"))
boton6 = Button(ventana, text="6", width=5, height=2, command=lambda: boton_numero("6"))
boton7 = Button(ventana, text="7", width=5, height=2, command=lambda: boton_numero("7"))
boton8 = Button(ventana, text="8", width=5, height=2, command=lambda: boton_numero("8"))
boton9 = Button(ventana, text="9", width=5, height=2, command=lambda: boton_numero("9"))

boton_borrar_todo = Button(ventana, text="AC", width=5, height=2, command=borrar_todo)
boton_abrir_parentesis = Button(ventana, text="(", width=5, height=2, command=lambda: boton_numero("("))
boton_cerrar_parentesis = Button(ventana, text=")", width=5, height=2, command=lambda: boton_numero(")"))
boton_punto = Button(ventana, text=".", width=5, height=2, command=lambda: boton_numero("."))
boton_borrar_caracter = Button(ventana, text=chr(9003), width=5, height=2, command=borrar_caracter)

boton_div = Button(ventana, text=chr(247), width=5, height=2, command=lambda: boton_numero("/"))
boton_mult = Button(ventana, text="x", width=5, height=2, command=lambda: boton_numero("*"))
boton_sum = Button(ventana, text="+", width=5, height=2, command=lambda: boton_numero("+"))
boton_rest = Button(ventana, text="-", width=5, height=2, command=lambda: boton_numero("-"))
boton_igual = Button(ventana, text="=", width=5, height=2, command=hacer_operacion)

# Agregando botones
boton_borrar_todo.grid(row=1, column=0, padx=5, pady=5)
boton_abrir_parentesis.grid(row=1, column=1, padx=5, pady=5)
boton_cerrar_parentesis.grid(row=1, column=2, padx=5, pady=5)
boton_borrar_caracter.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_div.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_mult.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_sum.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, padx=5, pady=5)
boton_punto.grid(row=5, column=1, padx=5, pady=5)
boton_igual.grid(row=5, column=2, padx=5, pady=5)
boton_rest.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()
