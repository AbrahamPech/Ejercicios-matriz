import random
import os

class Invertir:

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def main():
        while True:
            Invertir.clear_screen()
            try:
                size = int(input("¿De qué tamaño será el arreglo que quieres invertir? (mínimo 1): "))
                if size < 1:
                    raise ValueError("El tamaño del arreglo debe ser al menos 1")
                break
            except ValueError:
                print("Error: Ingrese un número entero válido mayor o igual a 1.")
                input("Presione Enter para continuar...")

        Invertir.clear_screen()
        arreglo = []
        while True:
            try:
                opcion = int(input("¿Quieres llenar el arreglo manual o automático?\n1.-Manual\n2.-Automático\nOpción: "))
                if opcion not in [1, 2]:
                    raise ValueError("Opción no válida")
                break
            except ValueError:
                print("Error: Ingrese 1 o 2.")
                input("Presione Enter para continuar...")
                Invertir.clear_screen()

        Invertir.clear_screen()
        if opcion == 1:
            for i in range(size):
                while True:
                    try:
                        numeroManual = int(input(f"Ingrese el número {i+1}: "))
                        arreglo.append(numeroManual)
                        break
                    except ValueError:
                        print("Error: Ingrese un número entero válido.")
                        input("Presione Enter para continuar...")
                        Invertir.clear_screen()
        else:
            arreglo = [random.randint(0, 100) for _ in range(size)]

        arregloInvertido = arreglo[::-1]
        Invertir.clear_screen()
        print(f"El arreglo original es {arreglo}")
        print(f"El arreglo invertido es {arregloInvertido}")
