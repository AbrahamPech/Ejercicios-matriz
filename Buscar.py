import random
import os

class Buscar:

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def main():
        while True:
            Buscar.clear_screen()
            try:
                filas = int(input("¿De cuántas filas quieres la matriz? (mínimo 1): "))
                if filas < 1:
                    raise ValueError("El número de filas debe ser al menos 1")
                columnas = int(input("¿De cuántas columnas quieres la matriz? (mínimo 1): "))
                if columnas < 1:
                    raise ValueError("El número de columnas debe ser al menos 1")
                break
            except ValueError as e:
                print(f"Error: Ingrese un número entero válido. {str(e)}")
                input("Presione Enter para continuar...")

        matriz = Buscar.generarMatriz(filas, columnas)
        
        while True:
            Buscar.clear_screen()
            try:
                elemento = int(input("Ingresa el número que buscas: "))
                break
            except ValueError:
                print("Error: Ingrese un número entero válido.")
                input("Presione Enter para continuar...")

        posicion, existe = Buscar.buscarElemento(matriz, elemento)

        Buscar.clear_screen()
        if existe:
            print(f"Sí existe en la posición: fila {posicion[0] + 1}, columna {posicion[1] + 1}")
        else:
            print("No existe")

        print("\nMatriz generada:")
        for fila in matriz:
            print(fila)


    @staticmethod
    def generarMatriz(filas, columnas):
        return [[random.randint(0, 20) for _ in range(columnas)] for _ in range(filas)]
    
    @staticmethod
    def buscarElemento(matriz, elemento):
        for i, fila in enumerate(matriz):
            for j, valor in enumerate(fila):
                if valor == elemento:
                    return ([i, j], True)
        return ([], False)

