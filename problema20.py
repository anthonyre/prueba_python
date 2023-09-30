class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "No se puede dividir por cero."

# Ejemplos de uso de los métodos estáticos de la clase Calculadora
resultado_suma = Calculadora.sumar(5, 3)
print("Suma:", resultado_suma)

resultado_resta = Calculadora.restar(10, 7)
print("Resta:", resultado_resta)

resultado_multiplicacion = Calculadora.multiplicar(4, 6)
print("Multiplicación:", resultado_multiplicacion)

resultado_division = Calculadora.dividir(8, 2)
print("División:", resultado_division)
