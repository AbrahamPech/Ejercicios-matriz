from Invertir import Invertir 
from Buscar import Buscar
from Pesos import Pesos
from Promedios import Promedios

while True:
    print("Menu")
    print("1.- Invertir arreglo")
    print("2.- Buscar un dato")
    print("3.- Peso de 10 personas")
    print("4.- Promedios de alumnos")
    print("5.- Sueldos empleados")
    print("0.- Salir del programa")
    opcion = input("Seleccionar: ")

    if opcion == '0':
        break
    elif opcion == '1':
        Invertir.main()
    elif opcion == '2':
        Buscar.main()
    elif opcion == '3':
        Pesos.main()
    elif opcion == '4':
        Promedios.main()
    else:
        print("nada")    
