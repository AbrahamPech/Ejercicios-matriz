import random

class Invertir:

    def main():
        arreglo = []
        size = int(input("De que tamaño sera el arreglo que quieres invertir?\n:"))
        while True:
            opcion = input("Quieres llenar el arreglo manual o automatico\n1.-Manual\n2.-Automatico\nOpcion:")
            if opcion == '1':
                for i in range(size):
                    numeroManual = int(input("Ingrese el numero:"))
                    arreglo.append(numeroManual)
                break
            elif opcion == '2':
                for i in range(size):
                    numeroRandom =  random.randint(0,100)
                    arreglo.append(numeroRandom)
                break
            else:
                print("la opcion ingresada no es valida")

        arregloInvertido = arreglo[::-1]
        print(f"El arreglo original es {arreglo}")
        print(f"El arreglo invertido es {arregloInvertido}")
