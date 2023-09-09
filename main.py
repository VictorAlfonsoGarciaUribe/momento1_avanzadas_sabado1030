from registrar_usuario import registrar_usuario
from tomar_bicicleta import tomar_bicicleta
from consultar_usuarios import consultar_usuarios
from consultar_prestamos import consultar_prestamos

# Inicializar las listas de usuarios y préstamos de bicicletas
usuarios = []
prestamos_bicicletas = []

# Menú principal
while True:
    print("\n***MENU***")
    print("1. Registrar Usuario")
    print("2. Tomar Bicicleta en Préstamo")
    print("3. Consultar Listado de Usuarios")
    print("4. Consultar Listado de Préstamos")
    print("5. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        usuarios = registrar_usuario(usuarios)
    elif opcion == "2":
        if not usuarios:
            print("Debe registrar usuarios antes de utilizar esta opción.")
        else:
            prestamos_bicicletas = tomar_bicicleta(usuarios,prestamos_bicicletas)
    elif opcion == "3":
        if not usuarios:
            print("Debe registrar usuarios antes de utilizar esta opción.")
        else:
            consultar_usuarios(usuarios)
    elif opcion == "4":
        if not prestamos_bicicletas:
            print("Debe tomar bicicletas en préstamo antes de utilizar esta opción.")
        else:
            consultar_prestamos(prestamos_bicicletas)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5).")
