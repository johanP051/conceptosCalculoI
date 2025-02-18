# Use el método de la bisección para encontrar una aproximación a la raı́z de la ecuación f (x) = x^3 −x−2 en el intervalo [1, 2] con una tolerancia de 10^(−3)

import numpy as np
from decimal import Decimal, getcontext

getcontext().prec = 50  #Se le da una precisión alta como un Double float de C++

class Biseccion():
    def __init__(self):
        pass

    def insertar_ecuacion(self):
        gradoPolinomio = int(input("Inserte el grado del polinomio: "))
        self.coeficientes = []

        for i in reversed(range(gradoPolinomio + 1)):
            coeficiente = Decimal(input(f"Inserte el coeficiente de x^{i}: "))
            self.coeficientes.append(coeficiente)
    
    def insertarIntervalo(self):
        print("Ahora debe insertar los intervalos \n")
        self.a = Decimal(input("Inserte el valor de [a]: "))
        self.b = Decimal(input("Inserte el valor de [b]: "))

    def evaluar_funcion(self, x):
        x = Decimal(x)
        return np.polyval(self.coeficientes, x)
    
    def calcularRaiz(self):
        self.x_inf = self.a
        self.x_sup = self.b

        while True:
            x_a = (self.x_sup + self.x_inf) / 2
            signo = self.evaluar_funcion(self.x_inf) * self.evaluar_funcion(x_a)

            ## Haciendo el cambio de límites de intervalos
            if signo < 0:
                self.x_sup = x_a
            else:
                self.x_inf = x_a

            error = self.evaluar_funcion(x_a)

            if abs(error) <= Decimal('1E-3'):
                print(f"Resultado de la raíz: {x_a}")
                break
            print(x_a)

ec = Biseccion()
ec.insertar_ecuacion()
ec.insertarIntervalo()
ec.calcularRaiz()