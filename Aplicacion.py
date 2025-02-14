
from Usuario import Usuario

class Aplicacion:
    def __init__(Aplicacion):
        Aplicacion.usuarios = {}  # Diccionario de usuarios registrados
       # Aplicacion.pago = Pago()  # Instancia de la clase pago
       
       #jacome y jotuel
       
    
    def registrar_usuario(Aplicacion, id_usuario, nombre, numero_cuenta, nip, saldo_inicial=0):
        """ Registra un nuevo usuario en el sistema. """
        if numero_cuenta in Aplicacion.usuarios:
            print("Error: La cuenta ya existe.")
            return
        Aplicacion.usuarios[numero_cuenta] = Usuario(id_usuario, nombre, numero_cuenta, nip, saldo_inicial)
        print(f"Usuario {nombre} registrado con éxito.")
    

    def iniciar_sesion(Aplicacion):
        
        try:
            """ Permite al usuario ingresar su número de cuenta y NIP para iniciar sesión. """
            numero_cuenta = input("Ingrese su número de cuenta: ")
            
            if not numero_cuenta.isdigit():
                        raise ValueError("El número de cuenta debe contener solo números.")
                    
            nip = input("Ingrese su NIP: ")
            if not nip.isdigit():
                        raise ValueError("El número de cuenta debe contener solo números.")

            if numero_cuenta in Aplicacion.usuarios and Aplicacion.usuarios[numero_cuenta].iniciar_sesion(nip):
                print("Inicio de sesión exitoso.")
                Aplicacion.mostrar_menu(Aplicacion.usuarios[numero_cuenta])
            else:
                print("Número de cuenta o NIP incorrecto.")
        except ValueError:
            print("-------------------------------------------------------------------------------")
            print("Ingresa una opción válida en tui nip / solo numeros.")
    
   
    def menuI(Aplicacion):
        elec = -1
        while elec !=0:
            print("---------------------------------------------------------------------------------")
            print("1. INICIAR SESION") 
            print("2. Registrar")
            
            try:
                elec = int(input("Elige una opción: "))
                
            except ValueError:
                print("-------------------------------------------------------------------------------")
                print("Ingresa una opción válida.")
            
            if elec == 1:
                
                Aplicacion.iniciar_sesion()
                
            elif elec == 2: 
                try:
                    nombre = input("Ingresa tu nombre: ")
                    
                    numero_cu = input("Ingresa tu numero de cuenta: ")
                    
                        # Validar que el número de cuenta sea un número
                    if not numero_cu.isdigit():
                        raise ValueError("El número de cuenta debe contener solo números.")
                    
                    niip = input("Ingresa tu nip: ")
                    if not niip.isdigit():
                        raise ValueError("El número de cuenta debe contener solo números.")
                    
                    saldo = 1000
                    # len(Aplicacion.usuarios) + 1 / sirve para auto incrementar la id
                    Aplicacion.registrar_usuario(len(Aplicacion.usuarios) + 1, nombre, numero_cu, niip, saldo)
                    
                except ValueError:
                    
                    print("-------------------------------------------------------------------------------")
                    print("Ingresa una opción válida / solo numeros positivos =).")


                
                
            else:
                
                print("-------------------------------------------------------------------------------")
                
                print("Selecciona solo los numeros mostrados")



    def mostrar_menu(Aplicacion):
         option = 0

         while option !=0:
            print("------------------------------------------------------------------------------")
            print("1.Consultar Saldo")
            print("2.Depositos")
            print("3.Retiros en Efectivo")
            print("4.Cambiar NIP")
            print("5.Transferencias")
            print("6.Pagos de Servicios")
            print("7.Generar Pagos")
            print("8.Cobros")
            print("9.Visualizar Pagos")
            print("10.Agregar Contactos")
            print("11.Eliminar Contactos")
            print("12.Salir")


            try:
                option = int(input("Elige una opción: "))
                
            except ValueError:
                print("-------------------------------------------------------------------------------")
                print("Opcion Invalida.")


                if option == 1: 
                    Aplicacion.Consultar_Saldo()
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
                    print("Cerrando sesion...")
                    break
                else:
                    print("-------------------------------------------------------------------------------")
                    print("Selecciona una opcion valida.")

            except ValueError:
                print("-------------------------------------------------------------------------------")
                print("Opcion invalida. Ingresa una opcion valido.")
            
                 


    