class Transaccion:
    def __init__(self, tipo, monto, cuenta_origen, cuenta_destino=None):
        self.tipo = tipo
        self.monto = monto
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino

    def validar_transaccion(self):
        # Verifica si la transacción es válida
        if self.tipo not in ["Depósito", "Retiro", "Transferencia"]:
            return False
        if self.monto <= 0:
            return False
        if self.tipo == "Transferencia" and self.cuenta_destino is None:
            return False
        # Aquí puedes agregar más validaciones, como verificar fondos suficientes
        return True

    def ejecutar_transaccion(self):
        if not self.validar_transaccion():
            return "Transacción no válida"
        
        if self.tipo == "Depósito":
            # Lógica para depositar en la cuenta de origen
            pass
        elif self.tipo == "Retiro":
            # Lógica para retirar de la cuenta de origen
            pass
        elif self.tipo == "Transferencia":
            # Lógica para transferir de la cuenta de origen a la cuenta de destino
            pass
        return "Transacción ejecutada con éxito"