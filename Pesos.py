import os

class Pesos:
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def main():
        pesos = []
        for i in range(10):
            while True:
                Pesos.clear_screen()
                try:
                    peso = float(input(f"Ingrese el peso de la persona {i+1} (en kg): "))
                    if peso <= 0:
                        raise ValueError("El peso debe ser un número positivo")
                    pesos.append(peso)
                    break
                except ValueError:
                    print("Error: Ingrese un número válido positivo. No se permiten letras.")
                    input("Presione Enter para continuar...")

        Pesos.clear_screen()
        promedio = Pesos.obtenerPromedio(pesos)
        print(f"\nEl promedio de los pesos es: {promedio:.2f}")

        mayores = Pesos.contarMayoresQuePromedio(pesos, promedio)
        print(f"{mayores} personas tienen un peso mayor al promedio.")

        menores = Pesos.contarMenoresQuePromedio(pesos, promedio)
        print(f"{menores} personas tienen un peso menor al promedio.")
    
    @staticmethod
    def obtenerPromedio(pesos):
        return sum(pesos) / len(pesos)

    @staticmethod
    def contarMayoresQuePromedio(pesos, promedio):
        return sum(1 for peso in pesos if peso > promedio)

    @staticmethod
    def contarMenoresQuePromedio(pesos, promedio):
        return sum(1 for peso in pesos if peso < promedio)

