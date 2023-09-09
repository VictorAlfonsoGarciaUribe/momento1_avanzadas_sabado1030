def registrar_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario: ")# ingresar el nombre
    numero_tarjeta = input("Ingrese el número de tarjeta: ")# ingresar el número de tarjeta
    
    usuarios.append([nombre, numero_tarjeta]) # agrega la información a lista de usuarios
    
    print(f"Usuario registrado: {nombre} - Tarjeta: {numero_tarjeta}")# confirmando el registro del usuario
    return usuarios; 
    

