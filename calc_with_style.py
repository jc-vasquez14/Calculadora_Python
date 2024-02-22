import re
from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
ventana.configure(bg="#f0f0f0")

i = 0

# Entrada
e_texto = Entry(ventana, font=("Helvetica", 20), borderwidth=2, relief="solid", justify="right")
e_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Funciones
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
    try:
        ecuacion = e_texto.get()
        resultado = eval(ecuacion)
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
        i = 0
    except Exception as e:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")

# Validación de entrada
def validar_entrada(entrada):
    patron = r'^[0-9+*./()-]*$'
    return re.match(patron, entrada) is not None

# Botones
def boton_numero(valor):
    if validar_entrada(valor):
        click_boton(valor)

boton0 = Button(ventana, text="0", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("0"))
boton1 = Button(ventana, text="1", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("1"))
boton2 = Button(ventana, text="2", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("2"))
boton3 = Button(ventana, text="3", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("3"))
boton4 = Button(ventana, text="4", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("4"))
boton5 = Button(ventana, text="5", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("5"))
boton6 = Button(ventana, text="6", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("6"))
boton7 = Button(ventana, text="7", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("7"))
boton8 = Button(ventana, text="8", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("8"))
boton9 = Button(ventana, text="9", width=7, height=2, font=("Helvetica", 14), command=lambda: boton_numero("9"))

boton_borrar_todo = Button(ventana, text="AC", width=7, height=2, font=("Helvetica", 14), bg="#ffcccc", command=borrar_todo)
boton_abrir_parentesis = Button(ventana, text="(", width=7, height=2, font=("Helvetica", 14), bg="#ccffcc", command=lambda: boton_numero("("))
boton_cerrar_parentesis = Button(ventana, text=")", width=7, height=2, font=("Helvetica", 14), bg="#ccffcc", command=lambda: boton_numero(")"))
boton_punto = Button(ventana, text=".", width=7, height=2, font=("Helvetica", 14), bg="#ccffcc", command=lambda: boton_numero("."))
boton_borrar_caracter = Button(ventana, text=chr(9003), width=7, height=2, font=("Helvetica", 14), bg="#ffcccc", command=borrar_caracter)

boton_div = Button(ventana, text="÷", width=7, height=2, font=("Helvetica", 14), bg="#ccffcc", command=lambda: boton_numero("/"))
boton_mult = Button(ventana, text="×", width=7, height=2, font=("Helvetica", 14), bg="#ccffcc", command=lambda: boton_numero("*"))
boton_sum = Button(ventana, text="+", width=7, height=2, font=("Helvetica", 14), bg="#ccffcc", command=lambda: boton_numero("+"))
boton_rest = Button(ventana, text="-", width=7, height=2, font=("Helvetica", 14), bg="#ccffcc", command=lambda: boton_numero("-"))
boton_igual = Button(ventana, text="=", width=7, height=2, font=("Helvetica", 14), bg="#66ccff", command=hacer_operacion)

# Agregando botones
boton_borrar_todo.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
boton_abrir_parentesis.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
boton_cerrar_parentesis.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
boton_borrar_caracter.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

boton7.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
boton8.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
boton9.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
boton_div.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

boton4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
boton5.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
boton6.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
boton_mult.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

boton1.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
boton2.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
boton3.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
boton_sum.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

boton0.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
boton_punto.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
boton_igual.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
boton_rest.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)
ventana.grid_columnconfigure(3, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_rowconfigure(3, weight=1)
ventana.grid_rowconfigure(4, weight=1)
ventana.grid_rowconfigure(5, weight=1)

ventana.mainloop()

