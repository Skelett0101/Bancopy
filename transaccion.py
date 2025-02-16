class Transaccion:
    def __init__(Transaccion, tipo, monto, cuenta_origen, cuenta_destino=None):
        Transaccion.tipo = tipo  # "Depósito", "Retiro", "Transferencia"
        Transaccion.monto = monto
        Transaccion.cuenta_origen = cuenta_origen
        Transaccion.cuenta_destino = cuenta_destino

    def validar_transaccion(Transaccion):
        """ Verifica si la transacción es válida (fondos suficientes, monto permitido). """
        if Transaccion.tipo == "Retiro" and Transaccion.monto > Transaccion.cuenta_origen.saldo:
            print("Error: Fondos insuficientes para el retiro.")
            return False
        if Transaccion.tipo == "Transferencia":
            if Transaccion.monto > 15000:
                print("Error: No puedes transferir más de $15,000.")
                return False
            if Transaccion.monto > Transaccion.cuenta_origen.saldo:
                print("Error: Fondos insuficientes para la transferencia.")
                return False
        return True

    def ejecutar_transaccion(Transaccion):
        """ Realiza la operación si es válida. """
        if not Transaccion.validar_transaccion():
            return False

        if Transaccion.tipo == "Depósito":
            Transaccion.cuenta_origen.depositar(Transaccion.monto)
        elif Transaccion.tipo == "Retiro":
            Transaccion.cuenta_origen.retirar(Transaccion.monto)
        elif Transaccion.tipo == "Transferencia":
            Transaccion.cuenta_origen.transferir(Transaccion.monto, Transaccion.cuenta_destino)

        print(f"Transacción {Transaccion.tipo} de ${Transaccion.monto} completada.")
        return True
