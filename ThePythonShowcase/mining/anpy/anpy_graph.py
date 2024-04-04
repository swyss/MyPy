import numpy as np
import matplotlib.pyplot as plt

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

class GraphClass:
    @staticmethod
    def plot_function(function, x_range, label=None):
        x = np.linspace(x_range[0], x_range[1], 400)
        y = np.vectorize(function)(x)  # Vectorize macht die Funktion für Arrays nutzbar
        plt.plot(x, y, label=label)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        if label:
            plt.legend()

    @staticmethod
    def plot_polynomial(polynomial, x_range, label=None):
        coeffs = polynomial.coefficients[::-1]  # Umkehren der Koeffizienten für np.polyval
        x = np.linspace(x_range[0], x_range[1], 400)
        y = np.polyval(coeffs, x)
        plt.plot(x, y, label=label)
        plt.xlabel('x')
        plt.ylabel('P(x)')
        if label:
            plt.legend()

    @staticmethod
    def show():
        plt.grid(True)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.show()

# Beispielanwendung:
if __name__ == "__main__":
    # Funktion plotten
    GraphClass.plot_function(np.sin, [-2*np.pi, 2*np.pi], 'sin(x)')
    
    # Polynom plotten
    p = PolynomialClass([1, 0, -2])  # Polynom x^2 - 2
    GraphClass.plot_polynomial(p, [-3, 3], 'x^2 - 2')
    
    # Grafik anzeigen
    GraphClass.show()
