import os
from Invertir import Invertir 
from Buscar import Buscar
from Pesos import Pesos
from Promedios import Promedios
from Empleado import Empleado

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    print("Menu")
    print("1.- Invertir arreglo")
    print("2.- Buscar un dato")
    print("3.- Peso de 10 personas")
    print("4.- Promedios de alumnos")
    print("5.- Sueldos empleados")
    print("0.- Salir del programa")
    
    try:
        opcion = int(input("Seleccionar: "))
        if opcion < 0 or opcion > 5:
            raise ValueError("Opción fuera de rango")
    except ValueError:
        print("Error: Ingrese un número válido entre 0 y 5.")
        input("Presione Enter para continuar...")
        continue

    clear_screen()
    if opcion == 0:
        break
    elif opcion == 1:
        Invertir.main()
    elif opcion == 2:
        Buscar.main()
    elif opcion == 3:
        Pesos.main()
    elif opcion == 4:
        Promedios.main()
    elif opcion == 5:
        Empleado.main()
    
    input("Presione Enter para volver al menú principal...")
