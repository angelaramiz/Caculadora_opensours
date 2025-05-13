from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("\nCalculadora Open Source")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar múltiples números")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {sumar(a, b)}")
            except ValueError:
                print("Error: Ingrese números válidos")

        elif opcion == '2':
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {restar(a, b)}")
            except ValueError:
                print("Error: Ingrese números válidos")

        elif opcion == '3':
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {multiplicar(a, b)}")
            except ValueError:
                print("Error: Ingrese números válidos")

        elif opcion == '4':
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                resultado = dividir(a, b)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Error: Ingrese números válidos")

        elif opcion == '5':
            try:
                numeros = list(map(float, input("Ingrese números separados por espacios: ").split()))
                if not numeros:
                    print("Error: Ingrese al menos un número")
                    continue
                print(f"Resultado: {suma_avanzada(*numeros)}")
            except ValueError:
                print("Error: Ingrese números válidos")

        elif opcion == '6':
            print("¡Gracias por usar la calculadora!")
            break

        else:
            print("Opción inválida. Por favor, seleccione del 1 al 6")

if __name__ == "__main__":
    main()
