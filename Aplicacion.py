
from Usuario import Usuario

class Aplicacion:
    def __init__(Aplicacion):
        Aplicacion.usuarios = {}  # Diccionario de usuarios registrados
       # Aplicacion.pago = Pago()  # Instancia de la clase pago
       
       
    
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
            nip = int(input("Ingrese su NIP: "))

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
                    
                    niip = int(input("Ingresa tu nip: "))
                    
                    saldo = 1000
                    # len(Aplicacion.usuarios) + 1 / sirve para auto incrementar la id
                    Aplicacion.registrar_usuario(len(Aplicacion.usuarios) + 1, nombre, numero_cu, niip, saldo)
                    
                except ValueError:
                    
                    print("-------------------------------------------------------------------------------")
                    print("Ingresa una opción válida / solo numeros positivos =).")


                
                
            else:
                
                print("-------------------------------------------------------------------------------")
                
                print("Selecciona solo los numeros mostrados")