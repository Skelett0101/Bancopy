from Cuenta import Cuenta

class Usuario:
    def __init__(Usuario, id_usuario, nombre, numero_cuenta, nip, saldo=0):
        Usuario.id_usuario = id_usuario
        Usuario.nombre = nombre
        Usuario.nip = nip
        Usuario.cuenta = Cuenta(numero_cuenta, saldo)
        Usuario.contactos = {}  # Diccionario de contactos para realizar transferencias

    def iniciar_sesion(Usuario, nip_ingresado):
        """ Verifica que el NIP ingresado sea correcto. """
        return Usuario.nip == nip_ingresado

    def consultar_saldo(Usuario):
        """ Muestra el saldo disponible en la cuenta. """
        print(f"Saldo actual: ${Usuario.cuenta.saldo}")

    def cambiar_nip(Usuario, nuevo_nip):
        """ Cambia el NIP del usuario. """
        Usuario.nip = nuevo_nip
        print("NIP actualizado correctamente.")

    def ver_contactos(Usuario):
        """ Muestra los contactos registrados del usuario. """
        if not Usuario.contactos:
            print("No tienes contactos guardados.")
        else:
            print("Contactos:")
            for nombre, cuenta in Usuario.contactos.items():
                print(f"{nombre}: {cuenta.numero_cuenta}")
    

    def agregar_contacto(Usuario, nombre, cuenta_destino, usuarios):
        """ Agrega un contacto para realizar transferencias sin duplicados. """

        # Verificar si la cuenta destino existe en el sistema
        if cuenta_destino.numero_cuenta not in usuarios:
            print(f"Error: La cuenta {cuenta_destino.numero_cuenta} no está registrada en el sistema.")
            return False

        # Verificar que no sea la propia cuenta del usuario
        if cuenta_destino == Usuario.cuenta:
            print("Error: No puedes agregar tu propia cuenta como contacto.")
            return False

        # Verificar si la cuenta ya está en los contactos
        for contacto in Usuario.contactos.values():
            if contacto.numero_cuenta == cuenta_destino.numero_cuenta:
                print(f"Error: La cuenta {cuenta_destino.numero_cuenta} ya está registrada como contacto.")
                return False

        # Agregar el contacto si la cuenta destino es válida y no duplicada
        Usuario.contactos[nombre] = cuenta_destino
        print(f"Contacto {nombre} agregado con la cuenta {cuenta_destino.numero_cuenta}.")
        return True
    

    def seleccionar_contacto(Usuario):
        """Muestra los contactos registrados del usuario en forma de menú para seleccionar uno."""

        # Obtener el número de cuenta del usuario
        numero_cuenta_usuario = Usuario.cuenta.numero_cuenta  

        if not Usuario.contactos:
            print("No tienes contactos guardados.")
            return None  # Retorna None si no hay contactos disponibles

        # Mostrar el menú con los contactos
        print(f"\nTu número de cuenta: {numero_cuenta_usuario}")
        print("Selecciona un contacto para transferir dinero:")
        
        contactos_lista = list(Usuario.contactos.items())  # Convertir contactos en una lista para acceso por índice
        
        for i, (nombre, cuenta) in enumerate(contactos_lista, start=1):
            print(f"{i}. {nombre} - {cuenta.numero_cuenta}")

        # Pedir al usuario que elija un contacto
        try:
            opcion = int(input("Ingresa el número del contacto: "))
            if 1 <= opcion <= len(contactos_lista):
                contacto_seleccionado = contactos_lista[opcion - 1][1]  # Obtener la cuenta destino
                print(f"Has seleccionado a {contactos_lista[opcion - 1][0]} con cuenta {contacto_seleccionado.numero_cuenta}")
                return contacto_seleccionado  # Devuelve la cuenta seleccionada
            else:
                print("Error: Selección inválida.")
                return None
        except ValueError:
            print("Error: Ingresa un número válido.")
            return None

