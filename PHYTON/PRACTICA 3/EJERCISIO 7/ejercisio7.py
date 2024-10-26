class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def imprimir_datos(self):
        print(f"Lado mayor: {self.lado_mayor()}")
        print(f"Tipo de triángulo: {self.tipo_triangulo()}")

def crear_triangulo():
    lado1 = float(input("Ingrese el tamaño del lado 1: "))
    lado2 = float(input("Ingrese el tamaño del lado 2: "))
    lado3 = float(input("Ingrese el tamaño del lado 3: "))
    return Triangulo(lado1, lado2, lado3)

if __name__ == "__main__":
    triangulo = crear_triangulo()  
    print("\nDatos del Triángulo:")
    triangulo.imprimir_datos()  
