class Pago:
    def __init__(pago):
        pago.pagos_pendientes = {}  # Diccionario para almacenar pagos pendientes
        pago.pagos_completados = {}  # Diccionario para pagos completados

    def generar_pago(pago, usuario_generador, monto):
        """ Crea un pago generando un código único. """
        codigo = str(len(pago.pagos_pendientes) + 1000)  # Código único
        pago.pagos_pendientes[codigo] = {
            "monto": monto,
            "generador": usuario_generador  # El usuario que recibirá el dinero cuando alguien pague
        }

        print(f"Pago generado con código: {codigo}, Monto: ${monto}")
        return codigo

    def cobrar_pago(pago, usuario_pagador, codigo):
        """ Permite que un usuario pague usando un código de pago generado por otro usuario. """
        if codigo in pago.pagos_pendientes:
            pago_info = pago.pagos_pendientes[codigo]
            monto = pago_info["monto"]
            usuario_generador = pago_info["generador"]

            # Validación para evitar que el pagador sea el mismo que el generador
            if usuario_pagador == usuario_generador:
                print("Error: No puedes cobrar un pago que tú mismo generaste.")
                return False

            # Verificar si el usuario que ingresa el código (pagador) tiene saldo suficiente
            if usuario_pagador.cuenta.saldo >= monto:
                usuario_pagador.cuenta.retirar(monto)  # Se descuenta al que paga
                usuario_generador.cuenta.depositar(monto)  # Se le transfiere al que generó el pago
                print(f"Pago de ${monto} transferido a {usuario_generador.nombre}.")
                
                # Mover el pago de "pendiente" a "completado"
                pago.pagos_completados[codigo] = pago_info
                del pago.pagos_pendientes[codigo]  # Eliminar de pagos pendientes

                print("Pago cobrado exitosamente.")
                return True
            else:
                print("No tienes suficiente saldo para completar el pago.")
                return False
        else:
            print("Código de pago inválido.")
            return False
