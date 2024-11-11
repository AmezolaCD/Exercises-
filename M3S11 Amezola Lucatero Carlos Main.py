# main.py

from M3S11 A import crear_lista, eliminar_elementos_duplicados

def main():
    print("Bienvenido al programa de creación y manipulación de listas.\n")
    
    # Pedir al usuario cuántas listas desea crear
    while True:
        try:
            num_listas = int(input("¿Cuántas listas deseas crear? "))
            if num_listas < 1:
                print("Debe haber al menos una lista.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Crear las listas
    listas = []
    for i in range(num_listas):
        nombre_lista = f"lista {i + 1}"
        listas.append(crear_lista(nombre_lista))

    # Imprimir las listas originales
    print("\nListas originales:")
    for i, lista in enumerate(listas, 1):
        print(f"Lista {i}: {lista}")

    # Eliminar elementos de las listas en función de las listas posteriores
    listas_actualizadas = eliminar_elementos_duplicados(listas)

    # Imprimir las listas actualizadas
    print("\nListas después de eliminar elementos duplicados de listas posteriores:")
    for i, lista in enumerate(listas_actualizadas, 1):
        print(f"Lista {i}: {lista}")

if __name__ == "__main__":
    main()
