def obtener_letra_anterior(letra):
    # Determinar la letra anterior, manejando casos especiales
    if letra.islower():  # Si la letra es minúscula
        return chr(ord(letra) - 1) if letra != 'a' else 'No hay anterior'
    elif letra.isupper():  # Si la letra es mayúscula
        return chr(ord(letra) - 1) if letra != 'A' else 'No hay anterior'
    return 'Carácter no válido'

def obtener_letra_siguiente(letra):
    # Determinar la letra siguiente, manejando casos especiales
    if letra.islower():  # Si la letra es minúscula
        return chr(ord(letra) + 1) if letra != 'z' else 'No hay siguiente'
    elif letra.isupper():  # Si la letra es mayúscula
        return chr(ord(letra) + 1) if letra != 'Z' else 'No hay siguiente'
    return 'Carácter no válido'

# Bucle infinito hasta que el usuario decida salir
while True:
    try:
        # Solicitar una letra al usuario
        letra = input("Ingrese una letra (escriba 'salir' para terminar el programa): ")
        
        # Condición de salida
        if letra.lower() == 'salir':
            print("Programa terminado.")
            break
        
        # Validar si se ingresó algo vacío
        if not letra:
            print("Error: No ha ingresado ningún valor. Por favor, ingrese una letra.")
            continue
        
        # Validar que el usuario ingrese solo una letra alfabética
        if len(letra) != 1 or not letra.isalpha():
            print("Error: Entrada no válida. Debe ingresar una sola letra del alfabeto.")
            continue
        
        # Obtener la letra anterior y siguiente
        letra_anterior = obtener_letra_anterior(letra)
        letra_siguiente = obtener_letra_siguiente(letra)

        # Mostrar el resultado
        print(f"Letra anterior: {letra_anterior}")
        print(f"Letra siguiente: {letra_siguiente}")

    except KeyboardInterrupt:
        print("\nPrograma interrumpido manualmente. Saliendo...")
        break
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}. Inténtelo nuevamente.")
