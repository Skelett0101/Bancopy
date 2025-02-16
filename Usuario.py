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

    def agregar_contacto(Usuario, nombre, cuenta_destino):
        """ Agrega un contacto para realizar transferencias. """
        Usuario.contactos[nombre] = cuenta_destino
        print(f"Contacto {nombre} agregado con la cuenta {cuenta_destino.numero_cuenta}.")
