import numpy as np

class PolynomialClass:
    def __init__(self, coefficients):
        self.coefficients = np.array(coefficients)
    
    def evaluate(self, x):
        return np.polyval(self.coefficients, x)
    
    def derivative(self):
        new_coefficients = np.polyder(self.coefficients)
        return PolynomialClass(new_coefficients)

class FunctionClass:
    def __init__(self, function):
        self.function = function
    
    def evaluate(self, x):
        return self.function(x)
    
    def derivative(self):
        # Hinweis: Dies verwendet eine einfache numerische Annäherung
        def df(x, h=1e-5):
            return (self.function(x + h) - self.function(x)) / h
        return FunctionClass(df)

class SolverClass:
    @staticmethod
    def solve_equation(function, x0):
        from scipy.optimize import fsolve
        return fsolve(function, x0)[0]
    
    # Weitere Methoden zur Lösung spezifischer Gleichungstypen können hier hinzugefügt werden

class CalculusClass:
    @staticmethod
    def limit(function, x_to, direction='both'):
        from scipy import optimize
        if direction == 'both':
            return optimize.approx_fprime([x_to], function, [1e-5])[0]
        elif direction == 'left':
            return optimize.approx_fprime([x_to - 1e-5], function, [1e-5])[0]
        else:  # right
            return optimize.approx_fprime([x_to + 1e-5], function, [1e-5])[0]
    
    @staticmethod
    def integrate(function, a, b):
        from scipy.integrate import quad
        result, _ = quad(function, a, b)
        return result
    
    # Weitere fortgeschrittene Berechnungsmethoden können hier hinzugefügt werden

# Beispielanwendung:
if __name__ == "__main__":
    # Erstellen und Evaluieren eines Polynoms
    p = PolynomialClass([1, 0, -2])  # Polynom x^2 - 2
    print(p.evaluate(2))  # Sollte 2 ergeben

    # Ableitung des Polynoms
    dp = p.derivative()
    print(dp.coefficients)  # Sollte die Koeffizienten der Ableitung ausgeben

    # Anwendung einer Funktion
    f = FunctionClass(np.sin)
    print(f.evaluate(np.pi/2))  # Sollte 1 ergeben

    # Ableitung der Funktion
    df = f.derivative()
    print(df.evaluate(np.pi/2))  # Sollte ungefähr 0 ergeben (Ableitung von sin ist cos, cos(pi/2) = 0)

    # Lösung einer Gleichung
    solution = SolverClass.solve_equation(np.cos, 0.5)
    print(solution)  # Sollte in der Nähe von pi/2 sein

    # Berechnung eines Integrals
    integral = CalculusClass.integrate(np.sin, 0, np.pi)
    print(integral)  # Sollte 2 ergeben (Integral von sin(x) von 0 bis pi)
