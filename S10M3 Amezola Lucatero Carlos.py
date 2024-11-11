def crear_lista(nombre_lista):
    """
    Crea una lista con elementos especificados por el usuario.
    Permite definir la longitud de la lista y agregar elementos uno por uno.
    
    Args:
        nombre_lista (str): El nombre de la lista a crear (para mensajes de usuario).
        
    Returns:
        list: La lista creada con elementos únicos, sin duplicados.
    """
    while True:
        try:
            longitud = int(input(f"¿Cuántos elementos quieres en la {nombre_lista}? "))
            if longitud < 0:
                print("La longitud debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    lista = []
    for i in range(longitud):
        while True:
            elemento = input(f"Ingrese el elemento {i + 1} de la {nombre_lista}: ").strip()
            if elemento:
                lista.append(elemento)
                break
            else:
                print("El elemento no puede estar vacío. Inténtalo de nuevo.")

    # Elimina duplicados y notifica al usuario
    lista_unica = list(set(lista))
    if len(lista) != len(lista_unica):
        print(f"Se eliminaron duplicados en la {nombre_lista}. Lista única: {lista_unica}")
    else:
        print(f"{nombre_lista.capitalize()} creada sin duplicados: {lista_unica}")
    return lista_unica

def eliminar_duplicados(lista1, lista2):
    """
    Elimina los elementos de la primera lista que también están en la segunda.
    
    Args:
        lista1 (list): La lista de la cual se eliminarán los elementos duplicados.
        lista2 (list): La lista que contiene los elementos a eliminar de lista1.
        
    Returns:
        list: La lista filtrada sin los elementos de la segunda lista.
    """
    return [item for item in lista1 if item not in lista2]

def main():
    print("Bienvenido al programa de manipulación de listas.\n")
    
    # Crear las dos listas
    lista1 = crear_lista("primera lista")
    lista2 = crear_lista("segunda lista")

    # Imprimir las listas originales
    print("\nLista 1 original:", lista1)
    print("Lista 2 original:", lista2)

    # Confirmar si se deben eliminar elementos de lista1 según lista2
    eliminar = input("\n¿Deseas eliminar los elementos de la Lista 2 en la Lista 1? (s/n): ").strip().lower()
    if eliminar == 's':
        lista1_filtrada = eliminar_duplicados(lista1, lista2)
        print("\nLista 1 después de eliminar elementos que están en Lista 2:", lista1_filtrada)
    else:
        print("\nNo se realizaron eliminaciones. La Lista 1 queda igual:", lista1)

if __name__ == "__main__":
    main()
