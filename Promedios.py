class Promedios:
    
    def main():
        cursos = {
            "Estructura de Datos": [],
            "Desarrollo de Aplicaciones": [],
            "Ingeniería de Software": [],
            "Administración de Base de Datos": [],
            "Inglés IV": []
        }
        
        # Registrar las notas de los 5 alumnos en cada curso
        for curso in cursos:
            print(f"\nIngresando las notas de {curso}:")
            for i in range(5):
                nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
                cursos[curso].append(nota)
        
        # Calcular el promedio de cada curso
        promedios = {curso: Promedios.calcularPromedio(notas) for curso, notas in cursos.items()}
        
        # Encontrar el mayor promedio
        mayor_promedio = max(promedios.values())
        
        # Encontrar los cursos con el mayor promedio
        cursos_con_mayor_promedio = [curso for curso, promedio in promedios.items() if promedio == mayor_promedio]
        
        print("\nPromedio de cada curso:")
        for curso, promedio in promedios.items():
            print(f"{curso}: {promedio:.2f}")
        
        print(f"\nEl mayor promedio es {mayor_promedio:.2f}, obtenido por:")
        for curso in cursos_con_mayor_promedio:
            print(f"- {curso}")

    @staticmethod
    def calcularPromedio(notas):
        return sum(notas) / len(notas)

