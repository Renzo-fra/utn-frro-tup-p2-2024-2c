class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero."

    def imprimir_resultados(self):
        print(f"Suma: {self.suma()}")
        print(f"Resta: {self.resta()}")
        print(f"Multiplicación: {self.multiplicacion()}")
        print(f"División: {self.division()}")

def crear_calculadora():
    valor1 = int(input("Ingrese el primer valor entero: "))
    valor2 = int(input("Ingrese el segundo valor entero: "))
    return Calculadora(valor1, valor2)

if __name__ == "__main__":
    calculadora = crear_calculadora()  
    print("\nResultados de las operaciones:")
    calculadora.imprimir_resultados()  
