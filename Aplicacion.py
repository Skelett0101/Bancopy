from Usuario import Usuario
from Pago import Pago
from Transaccion import Transaccion
from Cuenta import Cuenta


class Aplicacion:
    def __init__(Aplicacion):
        Aplicacion.usuarios = {}  # Diccionario de usuarios registrados
        Aplicacion.pago = Pago()  # Instancia de la clase Pago
    def menuI(Aplicacion):
        while True:
            print("----------------------------------------------")
            print("                MENÚ PRINCIPAL                ")
            print("----------------------------------------------")
            print("1) Iniciar sesión")
            print("2) Registrar usuario")
            print("0) Salir")
            print("----------------------------------------------")

            try:
                elec = int(input("Elige una opción: "))
            except ValueError:
                print("Error: Debes ingresar un número válido.")
                continue

            if elec == 1:
                Aplicacion.iniciar_sesion()
            elif elec == 2:
                Aplicacion.registrar_usuario()
            elif elec == 0:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Inténtalo de nuevo.")

    def registrar_usuario(Aplicacion):
        print("----------------------------------------------")
        print("            REGISTRO DE USUARIO               ")
        print("----------------------------------------------")
        nombre = input("Ingresa tu nombre: ")

        # Validación del número de cuenta (debe ser numérico y de al menos 6 dígitos)
        while True:
            numero_cuenta = input("Ingresa tu número de cuenta: ")
            if numero_cuenta.isdigit() and len(numero_cuenta) >= 6:
                if numero_cuenta in Aplicacion.usuarios:
                    print("Error: La cuenta ya existe. Intente con otro número.")
                else:
                    break
            else:
                print("Error: El número de cuenta debe contener solo números y tener al menos 6 dígitos.")

        # Validación del NIP (debe ser numérico y exactamente de 4 dígitos)
        while True:
            nip = input("Ingresa tu NIP: ")
            if nip.isdigit() and len(nip) == 4:
                break
            else:
                print("Error: El NIP debe contener exactamente 4 dígitos numéricos.")

        saldo_inicial = 1000
        Aplicacion.usuarios[numero_cuenta] = Usuario(len(Aplicacion.usuarios) + 1, nombre, numero_cuenta, nip, saldo_inicial)
        print(f"Usuario {nombre} registrado con éxito.")

    def iniciar_sesion(Aplicacion):
        print("----------------------------------------------")
        print("              INICIAR SESIÓN                  ")
        print("----------------------------------------------")
        numero_cuenta = input("Ingrese su número de cuenta: ")

        if not numero_cuenta.isdigit():
            print("Error: El número de cuenta debe contener solo números.")
            return
        
        nip = input("Ingrese su NIP: ")

        if numero_cuenta in Aplicacion.usuarios and Aplicacion.usuarios[numero_cuenta].iniciar_sesion(nip):
            print("Inicio de sesión exitoso.")
            Aplicacion.mostrar_menu(Aplicacion.usuarios[numero_cuenta])  # Aquí pasamos el usuario al menú
        else:
            print("Número de cuenta o NIP incorrecto.")

    def mostrar_menu(Aplicacion, usuario):
        option = -1

        while option != 0:
            
            print("----------------------------------------------")
            print("                  MENÚ                        ")
            print("----------------------------------------------")
            print("1) Consultar saldo")
            print("2) Depósito")
            print("3) Retiro de efectivo")
            print("4) Cambiar NIP")
            print("5) Transferir")
            print("6) Ver contactos")
            print("7) Generar Pago")
            print("8) Cobrar Pago")
            print("9) Agregar Contacto")
            print("10) Pago de Servicio")
            print("0) Cerrar sesión")
            print("----------------------------------------------")
            
            try:
                option = int(input("Elige una opción: "))
                
                if option == 1: 
                    usuario.Consultar_Saldo()
                elif option == 2:
                    Aplicacion.Depositos()
                elif option == 3:
                    Aplicacion.Retiros()
                elif option == 4:
                    Aplicacion.Cambiar_Nip()
                elif option == 5:
                    Aplicacion.Transferencias()
                    
                elif option == 6:
                   usuario.ver_contactos()
                
                elif option == 7:
                    print("----------------------------------------------")
                    print("              GENERAR PAGO                    ")
                    print("----------------------------------------------")

                    try:
                        monto = float(input("Ingrese monto a cobrar: "))
                        if monto > 0:
                            codigo = Aplicacion.pago.generar_pago(usuario, monto)
                            print(f"Comparte este código con el destinatario para completar el pago.")
                        else:
                            print("Error: El monto debe ser positivo.")
                    except ValueError:
                        print("Error: Ingrese un número válido.")
                        
                        
                        
                elif option == 8:
                    print("----------------------------------------------")
                    print("              COBRAR PAGO                     ")
                    print("----------------------------------------------")

                    codigo = input("Ingrese código de pago recibido: ")
                    
                    print("----------------------------------------------")
                    
                    if Aplicacion.pago.cobrar_pago(usuario, codigo):
                        print("")
                    else:
                        print("Error al cobrar el pago. Verifica el código o el saldo disponible.")



                elif option == 9:
                    print("----------------------------------------------")
                    print("              AGREGAR CONTACTO                ")
                    print("----------------------------------------------")
                    nombre = input("Nombre del contacto: ")
                    cuenta = input("Número de cuenta: ")
                    if cuenta.isdigit() and cuenta in Aplicacion.usuarios:
                        usuario.agregar_contacto(nombre, Aplicacion.usuarios[cuenta].cuenta)
                    else:
                        print("Cuenta no encontrada o formato incorrecto.")

                elif option == 10:
                    print("----------------------------------------------")
                    print("              PAGO DE SERVICIO                ")
                    print("----------------------------------------------")
                    print("1) Agua")
                    print("2) Electricidad")
                    print("3) Internet")
                    print("----------------------------------------------")

                    seleccion = input("Ingresa una opción: ")

                    if seleccion == "1":
                        servicio = "Agua"
                    elif seleccion == "2":
                        servicio = "Electricidad"
                    elif seleccion == "3":
                        servicio = "Internet"
                    else:
                        print("Opción inválida. Inténtalo de nuevo.")
                        continue

                    try:
                        monto = int(input("Digita el monto que pagarás: "))
                        if monto > 0:
                            usuario.cuenta.pagar_servicio(servicio, monto)
                        else:
                            print("Error: El monto debe ser positivo.")
                    except ValueError:
                        print("Error: Debes ingresar un número entero válido.")
                    

                elif option == 0:
                    print("Sesión cerrada.")
                    break
                else:
                    print("Opción no válida.")
                    
            except ValueError:
                print("Opción inválida. Inténtalo de nuevo.")