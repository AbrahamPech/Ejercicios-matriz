import os

class Promedios:
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def main():
        cursos = {
            "Estructura de Datos": [],
            "Desarrollo de Aplicaciones": [],
            "Ingeniería de Software": [],
            "Administración de Base de Datos": [],
            "Inglés IV": []
        }
        
        for curso in cursos:
            Promedios.clear_screen()
            print(f"\nIngresando las notas de {curso}:")
            for i in range(5):
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota del alumno {i+1} (0-10): "))
                        if nota < 0 or nota > 10:
                            raise ValueError("La nota debe estar entre 0 y 0")
                        cursos[curso].append(nota)
                        break
                    except ValueError:
                        print("Error: Ingrese una nota válida entre 0 y 10. No se permiten letras.")
                        input("Presione Enter para continuar...")
                        Promedios.clear_screen()
                        print(f"\nIngresando las notas de {curso}:")
        
        promedios = {curso: Promedios.calcularPromedio(notas) for curso, notas in cursos.items()}
        
        mayor_promedio = max(promedios.values())
        
        cursos_con_mayor_promedio = [curso for curso, promedio in promedios.items() if promedio == mayor_promedio]
        
        Promedios.clear_screen()
        print("\nPromedio de cada curso:")
        for curso, promedio in promedios.items():
            print(f"{curso}: {promedio:.2f}")
        
        print(f"\nEl mayor promedio es {mayor_promedio:.2f}, obtenido por:")
        for curso in cursos_con_mayor_promedio:
            print(f"- {curso}")

    @staticmethod
    def calcularPromedio(notas):
        return sum(notas) / len(notas)

