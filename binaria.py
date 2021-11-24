import random

def busqueda_binaria(lista, comienzo, final, objetivo) -> bool:
    
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == "__main__":
    height_of_list = int(input("De que tamaño es la lista? "))
    objetive = int(input("Que numero quieres encontrar? "))

    lista = sorted([random.randint(0, 100) for i in range(height_of_list)])
    encontrado = busqueda_binaria(lista, 0, len(lista), objetive)
    message = "esta" if encontrado else "no esta"

    print(lista)
    print(f"El elemento {objetive} {message} en la lista")