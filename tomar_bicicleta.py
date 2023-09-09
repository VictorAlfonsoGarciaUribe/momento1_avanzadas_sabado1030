def tomar_bicicleta(usuarios,prestamos_bicicletas):
    
    numero_tarjeta = input("Ingrese el número de tarjeta del usuario: ")# ingresar el número de tarjeta
    origen = input("Ingrese el origen del préstamo: ")# ingresar el origen del préstamo
    destino = input("Ingrese el destino del préstamo: ")# ingresar el destino del préstamo

    usuario_encontrado = False
    
    for usuario in usuarios: # busca al usuario en la lista de usuarios por su número de tarjeta
        if usuario[1] == numero_tarjeta:
            usuario_encontrado = True
            break

    if usuario_encontrado:
        prestamos_bicicletas.append([numero_tarjeta, origen, destino])# agrega la información del préstamo a la lista de préstamos
        print(f"Usuario con tarjeta {numero_tarjeta} ha tomado una bicicleta en préstamo desde {origen} hasta {destino}")# Iiprime un mensaje confirmando el préstamo de la bicicleta
    else:
        print(f"Usuario con tarjeta {numero_tarjeta} no encontrado")# Imprime un mensaje si el usuario no se encuentra en la lista
    return prestamos_bicicletas; 