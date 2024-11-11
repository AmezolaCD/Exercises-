import matplotlib.pyplot as plt

def solicitar_anio(mensaje):
    """Solicita al usuario un año, asegurándose de que sea un número entero."""
    while True:
        try:
            anio = int(input(mensaje))
            return anio
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingresa un año como un número entero.")

def solicitar_venta(anio):
    """Solicita la venta de un año específico y asegura que sea un valor numérico positivo."""
    while True:
        try:
            venta = float(input(f"Ingrese las ventas para el año {anio}: "))
            if venta < 0:
                print("❌ Las ventas no pueden ser negativas. Por favor, ingresa un valor positivo.")
            else:
                return venta
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingresa un número para las ventas.")

def obtener_rango_anios():
    """Solicita y valida el año inicial y final, asegurando que el rango sea correcto."""
    while True:
        anio_inicio = solicitar_anio("Ingresa el año inicial: ")
        anio_fin = solicitar_anio("Ingresa el año final: ")
        if anio_inicio <= anio_fin:
            return anio_inicio, anio_fin
        else:
            print("❌ El año inicial debe ser menor o igual al año final. Inténtalo de nuevo.")

def obtener_ventas(anios):
    """Obtiene las ventas para cada año en la lista de años especificada."""
    ventas = []
    for anio in anios:
        ventas.append(solicitar_venta(anio))
    return ventas

def confirmar_datos(anios, ventas):
    """Permite al usuario confirmar o corregir los datos de años y ventas ingresados."""
    print("\n🔍 Verifica los datos ingresados:")
    for anio, venta in zip(anios, ventas):
        print(f"Año: {anio}, Ventas: {venta}")
    while True:
        confirmacion = input("¿Los datos son correctos? (sí/no): ").strip().lower()
        if confirmacion == 'sí':
            return True
        elif confirmacion == 'no':
            print("Por favor, ingresa nuevamente los datos.")
            return False
        else:
            print("❌ Respuesta no válida. Ingresa 'sí' o 'no'.")

def graficar_ventas(anios, ventas):
    """Genera una gráfica de líneas para visualizar las ventas de cada año."""
    plt.style.use('seaborn-darkgrid')  # Elegir un estilo atractivo
    plt.figure(figsize=(10, 6))
    
    # Graficar las ventas con personalización avanzada
    plt.plot(anios, ventas, marker='o', color='#4B0082', linestyle='-', linewidth=2, markersize=7, markerfacecolor='#FFA500')
    plt.fill_between(anios, ventas, color='#DDA0DD', alpha=0.2)  # Área debajo de la línea para realce visual
    plt.title(f"Ventas del {anios[0]} al {anios[-1]}", fontsize=16, fontweight='bold')
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("Ventas", fontsize=12)
    plt.xticks(anios, rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    # Mostrar la gráfica
    plt.show()

def main():
    """Función principal para ejecutar el flujo completo del programa."""
    print("📊 Bienvenido al programa de gráfico de ventas.")
    
    while True:
        anio_inicio, anio_fin = obtener_rango_anios()
        anios = list(range(anio_inicio, anio_fin + 1))  # Generar lista de años
        ventas = obtener_ventas(anios)
        
        # Confirmar datos con el usuario
        if confirmar_datos(anios, ventas):
            break
    
    # Generar y mostrar la gráfica
    graficar_ventas(anios, ventas)
    print("✅ Gracias por usar el programa. ¡Esperamos que hayas obtenido la información que necesitas!")

# Ejecutar el programa
if __name__ == "__main__":
    main()
