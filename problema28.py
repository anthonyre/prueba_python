class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("La cantidad de depósito debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self.saldo:.2f}")
        elif cantidad <= 0:
            print("La cantidad de retiro debe ser mayor que cero.")
        else:
            print("Fondos insuficientes. No se puede realizar el retiro.")

    def verificar_saldo(self):
        print(f"Saldo actual de la cuenta de {self.titular}: ${self.saldo:.2f}")

# Ejemplo de uso de la clase CuentaBancaria
cuenta1 = CuentaBancaria("Juan")

cuenta1.depositar(1000)
cuenta1.verificar_saldo()

cuenta1.retirar(500)
cuenta1.verificar_saldo()

cuenta1.retirar(700)
cuenta1.verificar_saldo()
