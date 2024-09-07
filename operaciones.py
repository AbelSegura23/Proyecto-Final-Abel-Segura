#Funciones de operaciones disponibles para hacer en la calculadora

class operaciones: 

    PI = 3.141592653589793
    e = 2.718281828459045

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "No se puede dividir entre Cero"
        return a / b

    def cuadrado(self, a):
        return a * a

    def potencia(self, base, exponente):
        resultado = 1
        while exponente > 0:
            if exponente % 2 == 1:
                resultado *= base
            base *= base
            exponente //= 2
        return resultado

