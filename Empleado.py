class Empleado:
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
            nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
            empleados.append(nombre)
            
            ingresosQuincenales = []
            for mes in range(5):
                ingreso = float(input(f"Ingrese el ingreso quincenal del empleado {nombre} para el mes {mes+1}: "))
                Empleado.agregarIngresoQuincenal(ingresosQuincenales, ingreso)
            
            ingresosEmpleados.append(ingresosQuincenales)
        
        # Vector con ingreso acumulado para cada empleado
        ingresosAcumulados = []
        for ingresos in ingresosEmpleados:
            ingresoAcumulado = Empleado.calcularIngresoAcumulado(ingresos)
            ingresosAcumulados.append(ingresoAcumulado)
        
        # Mostrar total pagado en sueldos en los últimos 5 meses
        totalPagado = sum(ingresosAcumulados)
        print(f"\nTotal pagado en sueldos en los últimos 5 meses: {totalPagado}")
        
        # Obtener el empleado con el mayor ingreso acumulado
        empleadoMaxIngresos = Empleado.obtenerEmpleadoMaxIngresos(empleados, ingresosAcumulados)
        print(f"Empleado con mayor ingreso acumulado: {empleadoMaxIngresos}")
