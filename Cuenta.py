from Pago import Pago

class Cuenta:

    def __init__(Cuenta, numero_cuenta, saldo=0):
        Cuenta.numero_cuenta = numero_cuenta
        Cuenta.saldo = saldo
    
    def Depositos(Cuenta, monto):
        """ Verifica que el monto no exceda los $15,000. """
        #Importa el monto desde pagos para hacer la trasferencia
        Cuenta.Monto = (monto)
        if Cuenta.Monto.monto > 15000:
            print("Error: No se puede depositar más de $15,000 por transacción.")
        elif Cuenta.Monto.monto <= 0:
            print("Error: El monto a depositar debe ser mayor a 0.")
        else:
            Cuenta.saldo += Cuenta.Monto.monto
            print(f"Depósito exitoso. Nuevo saldo: ${Cuenta.saldo}")

    def Retiros(Cuenta, monto):
        #Ve que le monto no sa mayor al saldo
        """ Retira una cantidad de dinero de la cuenta, verificando que el saldo sea suficiente. """
        if Cuenta.Monto.monto > Cuenta.saldo:
            print("Error: Fondos insuficientes.")
        elif Cuenta.Monto.monto <= 0:
            print("Error: El monto a retirar debe ser mayor a 0.")
        else:
            Cuenta.saldo -= Cuenta.Monto.monto
            print(f"Retiro exitoso. Nuevo saldo: ${Cuenta.saldo}")

    def Transferencias(Cuenta, monto, cuenta_destino):
        """ Realiza una transferencia a otra cuenta. Verifica que el monto no exceda los límites y haya suficiente saldo en la cuenta. """
        if Cuenta.Monto.monto > Cuenta.saldo:
            print("Error: Fondos insuficientes para la transferencia.")
        elif Cuenta.Monto.monto <= 0:
            print("Error: El monto a transferir debe ser mayor a 0.")
        elif Cuenta.Monto.monto > 15000:
            print("Error: No se puede transferir más de $15,000 por transacción.")
        else:
            Cuenta.saldo -= Cuenta.Monto.monto
            cuenta_destino.saldo += Cuenta.Monto.monto
            print(f"Transferencia exitosa. Nuevo saldo: ${Cuenta.saldo}")