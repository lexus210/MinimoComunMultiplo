from src.logica.FaltanParametros import FaltanParametros

class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def calcularMCM(self):
        if len(self.__numeros) < 2:
            raise FaltanParametros("Se necesitan al menos dos números para calcular el MCM.")
        return self.MCMMasDosNumeros()

    def MCD(self, numero1, numero2):
        while numero2 != 0:
            numero1, numero2 = numero2, numero1 % numero2
        return numero1

    def MCM(self, numero1, numero2):
        return (numero1 * numero2) // self.MCD(numero1, numero2)

    def MCMMasDosNumeros(self):
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError(f"{n} no es un número válido.")

        mcm = self.MCM(self.__numeros[0], self.__numeros[1])
        for n in self.__numeros[2:]:
            mcm = self.MCM(mcm, n)
        return mcm
