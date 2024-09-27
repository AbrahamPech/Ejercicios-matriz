import random

class Buscar:

    def main():
        filas = int(input("¿De cuántas filas quieres la matriz?\n: "))
        columnas = int(input("¿De cuántas columnas quieres la matriz?\n: "))
        matriz = Buscar.generarMatriz(filas, columnas)
        elemento = int(input("Ingresa el número que buscas: "))

        existe = Buscar.buscarElemento(matriz, elemento)

        if existe:
            print("Sí existe")
        else:
            print("No existe")


    @staticmethod
    def generarMatriz(filas, columnas):
        return [[random.randint(0, 20) for _ in range(columnas)] for _ in range(filas)]
    
    @staticmethod
    def buscarElemento(matriz, elemento):
        for fila in matriz:
            if elemento in fila:
                return True
        return False

