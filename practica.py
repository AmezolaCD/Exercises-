# Número máximo de intentos antes de cerrar el programa
MAX_INTENTOS = 3

def es_contraseña_valida(contraseña):
    """
    Valida si la contraseña comienza con un número.
    """
    return contraseña and contraseña[0].isdigit()

def solicitar_contraseña():
    """
    Solicita al usuario que ingrese una contraseña válida que comience con un número.
    """
    while True:
        contraseña = input("Por favor, ingrese una contraseña que comience con un número: ")
        if es_contraseña_valida(contraseña):
            return contraseña
        print("Error: La contraseña debe comenzar con un número.")

def verificar_contraseña(contraseña_original):
    """
    Verifica que la contraseña ingresada coincida con la original.
    Permite hasta MAX_INTENTOS intentos antes de cerrar el programa.
    """
    for intento in range(1, MAX_INTENTOS + 1):
        contraseña_verificacion = input(f"Intento {intento}/{MAX_INTENTOS}. Ingrese nuevamente la contraseña para verificar: ")
        if contraseña_verificacion == contraseña_original:
            print("Contraseña verificada correctamente.")
            return True
        print(f"Error: Las contraseñas no coinciden. Inténtelo de nuevo.")
    
    print("Ha cometido tres errores al ingresar la contraseña. El programa se cerrará.")
    return False

def main():
    """
    Función principal que ejecuta el flujo del programa.
    """
    contraseña = solicitar_contraseña()
    if verificar_contraseña(contraseña):
        print("Proceso completado con éxito.")
    else:
        print("Programa terminado por errores repetidos.")

if __name__ == "__main__":
    main()
