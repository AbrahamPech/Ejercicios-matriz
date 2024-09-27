class Pesos:
    
    def main():
        # Crear un vector de 10 datos de tipo real que representan el peso de 10 personas
        pesos = []
        for i in range(10):
            peso = float(input(f"Ingrese el peso de la persona {i+1}: "))
            pesos.append(peso)

        # 1. Obtener el promedio de los pesos
        promedio = Pesos.obtenerPromedio(pesos)
        print(f"\nEl promedio de los pesos es: {promedio:.2f}")

        # 2. Contar cuántas personas tienen un peso mayor al promedio
        mayores = Pesos.contarMayoresQuePromedio(pesos, promedio)
        print(f"{mayores} personas tienen un peso mayor al promedio.")

        # 3. Contar cuántas personas tienen un peso menor al promedio
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

