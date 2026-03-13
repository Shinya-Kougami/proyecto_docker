# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    print("Ejecutando la calculadora...")
    print(f"Suma de 5 + 3 = {sumar(5, 3)}")
    print(f"Resta de 10 - 4 = {restar(10, 4)}")
    print(f"Multiplicación de 6 * 7 = {multiplicar(6, 7)}")
    print(f"División de 20 / 5 = {dividir(20, 5)}")