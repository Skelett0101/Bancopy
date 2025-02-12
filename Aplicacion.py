class Aplicacion:
    def __init__(Aplicacion):
        Aplicacion.usuarios = {}  # Diccionario de usuarios registrados
       # Aplicacion.pago = Pago()  # Instancia de la clase pago
   
   
    def menuI(Aplicacion):
        elec = -1
        while elec !=0:
            
            print("INICIAR SESION") 
            print("Registrar")
            elec = int(input("Elige una opcion: "))
            if elec == 1:
                Aplicacion.iniciar_sesion()
            elif elec == 2: 
                
                nombre = input("Ingresa tu nombre: ")
                numero_cu = input("Ingresa tu numero de cuenta: ")
                niip = input("Ingresa tu nip: ")
                saldo = 1000
                
                Aplicacion.registrar_usuario(len(Aplicacion.usuarios) + 1,nombre,numero_cu,niip,saldo)