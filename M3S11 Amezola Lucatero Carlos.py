# m_retosemanal.py

def crear_lista(nombre_lista):
    """
    Crea una lista con elementos especificados por el usuario, eliminando duplicados.
    
    Args:
        nombre_lista (str): El nombre de la lista para mostrar en los mensajes.
        
    Returns:
        list: Lista creada por el usuario sin duplicados.
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
    
    # Eliminar duplicados dentro de la lista
    lista_unica = list(set(lista))
    return lista_unica

def eliminar_elementos_duplicados(listas):
    """
    Elimina elementos de cada lista que también están en las listas posteriores.
    
    Args:
        listas (list): Lista de listas que serán procesadas.
        
    Returns:
        list: Lista de listas con elementos duplicados eliminados.
    """
    for i in range(len(listas) - 1):
        for j in range(i + 1, len(listas)):
            listas[i] = [item for item in listas[i] if item not in listas[j]]
    return listas
