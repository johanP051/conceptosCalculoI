import numpy as np

class DiferenciasFinitas():
    def __init__(self):
        pass

    def insertar_valores(self):
        self.x = float(input("Inserte el valor de x a evaluar en la derivada: "))
        self.h = float(input("Inserte el valor de h: "))

    def funcion(self, x):
        return np.exp(x)

    def derivada_Orden1(self, x, h):
        # f'(x) ≈ (f(x+h) - f(x)) / (h)
        return (self.funcion(x + h) - self.funcion(x)) / (h)

    def derivada_Orden4(self, x, h):
        # f'(x) ≈ [ -25f(x) + 48f(x + h) - 36f(x + 2h) + 16f(x + 3h) -3f(x + 4h) ] / (12h)
        return (-25*self.funcion(x) + 48*self.funcion(x + h) - 36*self.funcion(x + 2*h) + 16*self.funcion(x + 3*h) - 3*self.funcion(x + 4*h)) / (12*h) 

    def calcular_derivadas(self):
        d2 = self.derivada_Orden1(self.x, self.h)
        d4 = self.derivada_Orden4(self.x, self.h)

        #Para verificar se revisa que d/dx e^x sea aproximadamente e^x, como lo dice la teoria
        derivada_exacta = self.funcion(self.x)
        
        print(f"\nPara f(x) = e^x evaluada en 1 = {self.x}:")
        print(f"Derivada (diferencias finitas progresivas orden 2): {d2}")
        print(f"Derivada (diferencias finitas progresivas orden 4): {d4}")
        print(f"Derivada exacta: {derivada_exacta}")

dx = DiferenciasFinitas()
dx.insertar_valores()
dx.calcular_derivadas()
