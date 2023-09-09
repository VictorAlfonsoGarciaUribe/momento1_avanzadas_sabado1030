# consultar usuarios
def consultar_usuarios(usuarios):
    print("Listado de Usuarios:")
    for usuario in usuarios:# itera a través de la lista de usuarios e imprime su nombre y número de tarjeta
        print(f"Nombre: {usuario[0]}, Tarjeta: {usuario[1]}")
