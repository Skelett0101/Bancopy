class Pago:
    def __init__(self):
        self.pagos_pendientes = {}

    def generar_pago(self, usuario_origen, monto, usuario_destino):
        # Genera un código único para el pago
        codigo_pago = f"PAGO_{len(self.pagos_pendientes) + 1}"
        
        # Verifica si la cuenta de origen tiene fondos suficientes
        # Aquí deberías agregar la lógica para verificar los fondos
        if self.verificar_fondos(usuario_origen, monto):
            self.pagos_pendientes[codigo_pago] = {
                'monto': monto,
                'usuario_origen': usuario_origen,
                'usuario_destino': usuario_destino
            }
            return f"Pago generado con código: {codigo_pago}"
        else:
            return "Fondos insuficientes para generar el pago"

    def cobrar_pago(self, usuario_destino, codigo):
        if codigo in self.pagos_pendientes:
            pago = self.pagos_pendientes[codigo]
            monto = pago['monto']
            usuario_origen = pago['usuario_origen']
            
            # Lógica para mover el monto de la cuenta de origen a la de destino
            # Aquí deberías agregar la lógica para realizar la transferencia
            self.realizar_transferencia(usuario_origen, usuario_destino, monto)
            
            # Elimina el pago de la lista de pagos pendientes
            del self.pagos_pendientes[codigo]
            return f"Pago {codigo} cobrado exitosamente"
        else:
            return "Código de pago no válido"

    def verificar_fondos(self, usuario_origen, monto):
        # Lógica para verificar si la cuenta de origen tiene fondos suficientes
        # Esto es un placeholder, debes implementar la lógica real
        return True

    def realizar_transferencia(self, usuario_origen, usuario_destino, monto):
        # Lógica para realizar la transferencia
        # Esto es un placeholder, debes implementar la lógica real
        pass