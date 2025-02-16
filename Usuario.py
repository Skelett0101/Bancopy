from Cuenta import Cuenta

class Usuario:
    def __init__(Usuario, id_usuario, nombre, numero_cuenta, nip, saldo=0):
        Usuario.id_usuario = id_usuario
        Usuario.nombre = nombre
        Usuario.nip = nip
        Usuario.cuenta = Cuenta(numero_cuenta, saldo)
        Usuario.contactos = {}  # Diccionario de contactos para realizar transferencias
        Usuario.opcion_seleccionada = None
        ##es josue
        #papas
    

    def iniciar_sesion(Usuario, nip_ingresado):
        """ Verifica que el NIP ingresado sea correcto. """
        return Usuario.nip == nip_ingresado
    
    def consultar_saldo(Usuario):
        """Retorna el saldo actual de la cuenta."""
        try:
            return Usuario.cuenta.saldo
        except Exception as e:
            return f"Error al consultar el saldo: {e}"
    
    def cambiar_nip(Usuario, nuevo_nip):
        #Cambia el NIP del usuario con validaciones.
        try:
            if not nuevo_nip.isdigit():
                raise ValueError("El NIP solo puede contener números.")

            if len(nuevo_nip) != 4:
                raise ValueError("El NIP debe tener exactamente 4 dígitos.")

            if int(nuevo_nip) < 0:
                raise ValueError("El NIP no puede ser un número negativo.")

            Usuario.nip = nuevo_nip
            return "NIP cambiado exitosamente."
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Ocurrió un error inesperado: {e}"
        
    def ver_contactos(Usuario):
        """Muestra la lista de contactos."""
        try:
            return Usuario.contactos if Usuario.contactos else "No tienes contactos registrados."
        except Exception as e:
            return f"Error al ver contactos: {e}"
        
    def agregar_contacto(Usuario, nombre, cuenta_destino):
        #Agrega un contacto para transferencias
        try:
            if cuenta_destino in Usuario.contactos:
                return "El contacto ya existe."
            Usuario.contactos[cuenta_destino] = nombre
            return f"Contacto {nombre} agregado con éxito."
        except Exception as e:
            return f"Error al agregar contacto: {e}"
