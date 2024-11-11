# Función para validar si una entrada es un número entero
def pedir_entero(mensaje, min_valor=None, max_valor=None):
    while True:
        try:
            valor = int(input(mensaje))
            if min_valor is not None and valor < min_valor:
                raise ValueError(f"El valor debe ser mayor o igual a {min_valor}.")
            if max_valor is not None and valor > max_valor:
                raise ValueError(f"El valor debe ser menor o igual a {max_valor}.")
            return valor
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número válido.")

# Función para pedir opciones de 'si' o 'no'
def pedir_opcion_si_no(mensaje):
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion in ['si', 'no']:
            return opcion
        else:
            print("Por favor, ingrese 'si' o 'no'.")

# Iniciar la lista para almacenar la información de los alumnos
lista = []
alumnos = 0
max_alumnos = 6

# Bucle para agregar alumnos
while alumnos < max_alumnos:
    opcion = input('Agregar alumno (1) o terminar (2): ').strip()

    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno: ').capitalize()
        
        # Validar que la primera calificación sea un número válido
        calificacion1 = pedir_entero(f'Ingrese la primera calificación de {nombre} (0-100): ', 0, 100)

        # Preguntar si se desea ingresar una segunda calificación
        calificacion2 = pedir_opcion_si_no(f'Desea ingresar una segunda calificación para {nombre} (si/no): ')
        if calificacion2 == 'si':
            calificacion2 = pedir_entero(f'Ingrese la segunda calificación de {nombre} (0-100): ', 0, 100)
        else:
            calificacion2 = None
        
        # Preguntar si se desea ingresar una tercera calificación
        calificacion3 = pedir_opcion_si_no(f'Desea ingresar una tercera calificación para {nombre} (si/no): ')
        if calificacion3 == 'si':
            calificacion3 = pedir_entero(f'Ingrese la tercera calificación de {nombre} (0-100): ', 0, 100)
        else:
            calificacion3 = None
        
        # Crear una lista con las calificaciones no nulas
        calificaciones = [c for c in [calificacion1, calificacion2, calificacion3] if c is not None]
        
        # Calcular el promedio
        promedio = sum(calificaciones) / len(calificaciones)
        
        # Guardar el nombre, calificaciones y promedio del alumno
        alumno = [nombre, calificaciones, promedio]
        lista.append(alumno)
        alumnos += 1
        
    elif opcion == '2':
        print(f'El programa ha terminado con {alumnos} alumnos.')
        break
    
    else:
        print('Se ha ingresado una opción inválida. Por favor, intente nuevamente.')
        continue

# Mostrar la lista de alumnos con sus calificaciones y promedio
print('\nLa lista de alumnos es:')
for alumno in lista:
    nombre, calificaciones, promedio = alumno
    print(f'Alumno: {nombre} - Calificaciones: {calificaciones}, Promedio: {promedio:.2f}')
