class Pago:
    def __init__(Pago):
        Pago.pagos_pendientes = {}  # Diccionario para almacenar los pagos pendientes

    def generar_pago(Pago, usuario_origen, monto, usuario_destino):
        """ Crea un pago para un servicio, asignando un código único. """
        if usuario_origen.cuenta.saldo < monto:
            print("Saldo insuficiente para generar el pago.")
            return None

        codigo = str(len(Pago.pagos_pendientes) + 1000)  # Código único
        Pago.pagos_pendientes[codigo] = {
            "monto": monto,
            "origen": usuario_origen
        }

        print(f"Pago generado con código: {codigo}, Monto: ${monto}")
        return codigo

    def cobrar_pago(Pago, usuario_destino, codigo):
        """ Cobra un pago, moviendo el monto de la cuenta de origen a la de destino. """
        if codigo in Pago.pagos_pendientes:
            pago_info = Pago.pagos_pendientes.pop(codigo)
            monto = pago_info["monto"]
            usuario_origen = pago_info["origen"]

            if usuario_origen.cuenta.retirar(monto):
                usuario_destino.cuenta.depositar(monto)
                print(f"Pago de ${monto} cobrado exitosamente por {usuario_destino.nombre}.")
                return True
            else:
                print("No se pudo completar el pago por saldo insuficiente en la cuenta origen.")
                return False
        else:
            print("Código de pago inválido.")
            return False
