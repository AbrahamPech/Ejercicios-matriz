import os

class Empleado:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def agregarIngresoQuincenal(ingresosQuincenales, ingreso):
        ingresosQuincenales.append(ingreso)

    @staticmethod
    def calcularIngresoAcumulado(ingresosQuincenales):
        return sum(ingresosQuincenales)

    @staticmethod
    def obtenerEmpleadoMaxIngresos(empleados, ingresosAcumulados):
        maxIngreso = max(ingresosAcumulados)
        indiceMaximo = ingresosAcumulados.index(maxIngreso)
        return empleados[indiceMaximo]

    def main():
        empleados = []
        ingresosEmpleados = []
    
        for i in range(5):
            Empleado.clear_screen()
            nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
            empleados.append(nombre)
            
            ingresosQuincenales = []
            for mes in range(5):
                while True:
                    Empleado.clear_screen()
                    try:
                        ingreso = float(input(f"Ingrese el ingreso quincenal del empleado {nombre} para el mes {mes+1}: "))
                        if ingreso < 0:
                            raise ValueError("El ingreso no puede ser negativo")
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido. El ingreso no puede ser negativo ni contener letras.")
                        input("Presione Enter para continuar...")
                Empleado.agregarIngresoQuincenal(ingresosQuincenales, ingreso)
            
            ingresosEmpleados.append(ingresosQuincenales)
        
        ingresosAcumulados = []
        for ingresos in ingresosEmpleados:
            ingresoAcumulado = Empleado.calcularIngresoAcumulado(ingresos)
            ingresosAcumulados.append(ingresoAcumulado)
        
        Empleado.clear_screen()
        totalPagado = sum(ingresosAcumulados)
        print(f"\nTotal pagado en sueldos en los últimos 5 meses: {totalPagado}")

        empleadoMaxIngresos = Empleado.obtenerEmpleadoMaxIngresos(empleados, ingresosAcumulados)
        print(f"Empleado con mayor ingreso acumulado: {empleadoMaxIngresos}")
