from Usuario import Usuario
from Pago import Pago
from Transaccion import Transaccion
from Cuenta import Cuenta


class Aplicacion:
    def __init__(Aplicacion):
        Aplicacion.usuarios = {}  # Diccionario de usuarios registrados

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
            print("------------------------------------------------------------------------------")
            print("1. Consultar Saldo")
            print("2. Depositos")
            print("3. Retiros en Efectivo")
            print("4. Cambiar NIP")
            print("5. Transferencias")
            print("6. Pagos de Servicios")
            print("7. Generar Pagos")
            print("8. Cobros")
            print("9. Visualizar Pagos")
            print("10. Agregar Contactos")
            print("11. Eliminar Contactos")
            print("12. Salir")
            print("------------------------------------------------------------------------------")

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
                    Aplicacion.Pagos_de_Servicios()
                elif option == 7: 
                    Aplicacion.Generar_Pagos()
                elif option == 8:
                    Aplicacion.Cobros()
                elif option == 9:
                    Aplicacion.Visualizar_Pagos()
                elif option == 10:
                    Aplicacion.Agregar_Contactos()
                elif option == 11:
                    Aplicacion.Eliminar_Contactos()
                elif option == 0:
                    print("Cerrando sesión...")
                    break
                else:
                    print("Selecciona una opción válida.")
            except ValueError:
                print("Opción inválida. Ingresa una opción válida.")
