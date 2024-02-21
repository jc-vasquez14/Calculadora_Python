import re
import math

def calcular(operacion, num1, num2=None):
    if operacion == 'raiz':
        return math.sqrt(num1)
    elif operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        if num2 == 0:
            return "Error: No se puede dividir entre cero."
        else:
            return num1 / num2

def validar_numero(numero):
    return re.match(r'^-?\d+(\.\d+)?$', numero)

while True:
    operacion = input("Ingrese la operación (+, -, *, /, raiz) o 'salir' para terminar: ").strip().lower()
    if operacion == 'salir':
        break

    if operacion != 'raiz':
        num1 = input("Ingrese el primer número: ").strip()
        num2 = input("Ingrese el segundo número: ").strip()
        if not validar_numero(num1) or not validar_numero(num2):
            print("Entradas no válidas. Por favor, ingrese números enteros o decimales.")
            continue
        num1 = float(num1)
        num2 = float(num2)
    else:
        num1 = input("Ingrese el número para calcular la raíz cuadrada: ").strip()
        if not validar_numero(num1):
            print("Entrada no válida. Por favor, ingrese un número entero o decimal.")
            continue
        num1 = float(num1)

    if operacion == '/' and num2 == 0:
        print("Error: No se puede dividir entre cero.")
        continue

    resultado = calcular(operacion, num1, num2) if operacion != 'raiz' else calcular(operacion, num1)
    print("El resultado es:", resultado)