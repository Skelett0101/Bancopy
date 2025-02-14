from Cuenta import Cuenta

class Usuario:
    def __init__(Usuario, id_usuario, nombre, numero_cuenta, nip, saldo=0):
        Usuario.id_usuario = id_usuario
        Usuario.nombre = nombre
        Usuario.nip = nip
        Usuario.cuenta = Cuenta(numero_cuenta, saldo)
        Usuario.contactos = {}  # Diccionario de contactos para realizar transferencias
        ##es josue
        #papas
    def iniciar_sesion(Usuario, nip_ingresado):
        """ Verifica que el NIP ingresado sea correcto. """
        return Usuario.nip == nip_ingresado