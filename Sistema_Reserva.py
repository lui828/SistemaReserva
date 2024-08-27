usuarios = []
reservas = []

def registrar_usuario():
    nombre = input("Ingresa su nombre para registrar: ")
    if nombre in usuarios:
        print("El nombre de usuario ya está registrado, intentelo de nuevo.")
    else:
        usuarios.append(nombre)
        print(f"El Usuario {nombre} se registrado exitosamente.")
        print(" ")

def reservar_viaje():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    if nombre_usuario not in usuarios:
        print("Error: El usuario no está registrado.")
        return
    
    destino = input("Ingresa el destino del viaje: ")
    fecha = input("Ingresa la fecha del viaje (AAAA-MM-DD): ")
    
    reserva = {
        'nombre_usuario': nombre_usuario,
        'destino': destino,
        'fecha_viaje': fecha
    }
    reservas.append(reserva)
    print("Reserva realizada exitosamente.")
    print("  ")

def ver_reservas():
    nombre = input("Ingresa tu nombre de usuario para ver las reservas: ")
    if nombre not in usuarios:
        print("Error: El usuario no está registrado.")
        return
    
    reservas_usuario = [reserva for reserva in reservas if reserva['nombre_usuario'] == nombre]
    
    if not reservas_usuario:
        print("No tienes reservas.")
    else:
        print("Tus reservas:")
        for i, reserva in enumerate(reservas_usuario):
            print(f"{i}. Destino: {reserva['destino']}, Fecha: {reserva['fecha_viaje']}")
            print(" ")

def cancelar_reserva():
    nombre_usuario = input("Ingresa tu nombre de usuario para cancelar una reserva: ")
    if nombre_usuario not in usuarios:
        print("Error: El usuario no está registrado.")
        return
    
    reservas_usuario = [reserva for reserva in reservas if reserva['nombre_usuario'] == nombre_usuario]
    
    if not reservas_usuario:
        print("No tienes reservas para cancelar.")
        return
    
    print("Tus reservas:")
    for i, reserva in enumerate(reservas_usuario):
        print(f"{i}. Destino: {reserva['destino']}, Fecha: {reserva['fecha_viaje']}")
    
    try:
        reserva1 = int(input("Ingresa el numero de la reserva que deseas cancelar: "))
        if reserva1 < 0 or reserva1 >= len(reservas_usuario):
            print("El numero de la reserva no válido.")
            return
        
        reserva_a_cancelar = reservas_usuario[reserva1]
        
        reservas.remove(reserva_a_cancelar)
        print("Reserva cancelada exitosamente.")
    
    except ValueError:
        print("Por favor ingresa un número válido para el índice de reserva.")

def main():
    while True:
        print("Sistema de Gestión de Viajes")
        print("1. Registrar Usuario")
        print("2. Reservar un Viaje")
        print("3. Ver Reservas")
        print("4. Cancelar Reserva")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        
        elif opcion == '2':
            reservar_viaje()
        
        elif opcion == '3':
            ver_reservas()
        
        elif opcion == '4':
            cancelar_reserva()
        
        elif opcion == '5':
            print("Saliendo del programa....")
            break
        
        else:
            print("Opción no válida, por favor selecciona de nuevo.")

main()