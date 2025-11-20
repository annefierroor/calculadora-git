# Autores: Anne Sofia Fierro Ortiz & Alejandro Gomez Polanco
# Fecha: 2025
# Objetivo: Calculadora básica con validación

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def potencia(a, b):
    return a ** b

def validar_entrada(valor):
    try:
        return float(valor)
    except ValueError:
        return None

if __name__ == "__main__":
    print("🧮 Calculadora básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    opcion = input("Elige una opción (1-5): ")

    a = validar_entrada(input("Primer número: "))
    b = validar_entrada(input("Segundo número: "))

    if a is None or b is None:
        print("❌ Entrada inválida. Debes ingresar números.")
    else:
        if opcion == "1":
            print("✅ Resultado:", suma(a, b))
        elif opcion == "2":
            print("✅ Resultado:", resta(a, b))
        elif opcion == "3":
            print("✅ Resultado:", multiplicacion(a, b))
        elif opcion == "4":
            print("✅ Resultado:", division(a, b))
        elif opcion == "5":
            print("⚡ Resultado:", potencia(a, b))
        else:
            print("❌ Opción no válida")