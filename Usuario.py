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
         # Compara el NIP ingresado con el NIP del usuario y devuelve True si coinciden.
        return Usuario.nip == nip_ingresado
    
    def consultar_saldo(Usuario):
        """Retorna el saldo actual de la cuenta."""
        try:
             # Devuelve el saldo de la cuenta del usuario.
            return Usuario.cuenta.saldo
        except Exception as e:
            return f"Error al consultar el saldo: {e}"
    
    def cambiar_nip(Usuario, nuevo_nip):
        #Cambia el NIP del usuario con validaciones.
        try:
             # Verifica que el nuevo NIP contenga solo números.
            if not nuevo_nip.isdigit():
                raise ValueError("El NIP solo puede contener números.")
            # Verifica que el NIP tenga exactamente 4 dígitos.
            if len(nuevo_nip) != 4:
                raise ValueError("El NIP debe tener exactamente 4 dígitos.")

            # Asigna el nuevo NIP al usuario.
            Usuario.nip = nuevo_nip
            return "NIP cambiado exitosamente."
        
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Ocurrió un error inesperado: {e}"
        
    def ver_contactos(Usuario):
        #Muestra la lista de contactos
        try:
            # Verifica si el array contactos tiene elementos.
            # Si tiene contactos, los retorna. 
            # Si está vacío, devuelve un mensaje diciendo que no hay contactos.
            return Usuario.contactos if Usuario.contactos else "No tienes contactos registrados."
        except Exception as e:
            return f"Error al ver contactos: {e}"
        
    def agregar_contacto(Usuario, nombre, cuenta_destino):
        #Agrega un contacto para transferencias
        try:
            # Verifica si el contacto ingresado ya existe en los contactos del usuario.
            if cuenta_destino in Usuario.contactos:
                return "El contacto ya existe."
            
             # Si la cuenta no está en los contactos, la agrega con el nombre proporcionado.
            Usuario.contactos[cuenta_destino] = nombre
            return f"Contacto {nombre} agregado con éxito."
        except Exception as e:
            return f"Error al agregar contacto: {e}"
