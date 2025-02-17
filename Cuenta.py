class Cuenta:
    def __init__(Cuenta, numero_cuenta, saldo=0):
        Cuenta.numero_cuenta = numero_cuenta
        Cuenta.saldo = saldo

    def depositar(Cuenta, monto):
        """ Deposita una cantidad de dinero en la cuenta. Verifica que no exceda los $15,000. """
        if monto >= 15000:
            print("No puedes depositar más de $15,000 a la vez.")
            return False
        Cuenta.saldo += monto
        print(f"Depósito exitoso. ")
        return True

    def retirar(Cuenta, monto):
        """ Retira una cantidad de dinero de la cuenta, si el saldo es suficiente. """
        if monto > Cuenta.saldo:
            print("Saldo insuficiente.")
            return False
        Cuenta.saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${Cuenta.saldo}")
        return True

    def transferir(Cuenta, monto, cuenta_destino):
        """ Realiza una transferencia a otra cuenta, verificando que el monto no exceda el límite, haya suficiente saldo y que la cuenta destino sea válida. """
        
        # Verificar si la cuenta de destino es la misma que la cuenta de origen
        if Cuenta == cuenta_destino:
            print("Error: No puedes transferir dinero a tu propia cuenta.")
            return False

        # Verificar si la cuenta destino existe
        if cuenta_destino is None:
            print("Error: La cuenta destino no existe.")
            return False

        # Verificar el monto máximo de transferencia
        if monto > 15000:
            print("No puedes transferir más de $15,000 a la vez.")
            return False

        # Verificar que haya suficiente saldo
        if monto > Cuenta.saldo:
            print("Saldo insuficiente para la transferencia.")
            return False

        # Realizar la transferencia
        Cuenta.saldo -= monto
        cuenta_destino.depositar(monto)  # Deposita en la cuenta destino
        print(f"Transferencia exitosa de ${monto} a la cuenta {cuenta_destino.numero_cuenta}")
        return True
    
    def pagar_servicio(Cuenta, servicio, monto):
        """ Paga un servicio si hay saldo suficiente. """
        if monto > Cuenta.saldo:
            print(f"Saldo insuficiente para pagar {servicio}.")
            return False
        Cuenta.saldo -= monto
        print(f"Pago de {servicio} realizado con éxito. Nuevo saldo: ${Cuenta.saldo}")
        return True