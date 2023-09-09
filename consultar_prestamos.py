# consultar el listado de prestamos_bicicletas
def consultar_prestamos(prestamos_bicicletas):
    print("Listado de Préstamos:")
    for prestamo in prestamos_bicicletas:# Itera a través de la lista de prestamos_bicicletas e imprime la información del prestamos_bicicletas
        print(f"Tarjeta: {prestamo[0]}, Origen: {prestamo[1]}, Destino: {prestamo[2]}")

