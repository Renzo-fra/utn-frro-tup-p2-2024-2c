class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

    def evaluar(self):
        if self.nota >= 8:
            print(f"{self.nombre} ha sido promovido.")
        elif self.nota >= 6:
            print(f"{self.nombre} ha aprobado con recuperatorio.")
        elif self.nota >= 4:
            print(f"{self.nombre} es regular.")
        else:
            print(f"{self.nombre} está libre.")
    
def crear_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    nota_input = input(f"Ingrese la nota de {nombre}: ")
    nota = float(nota_input.replace(',', '.'))
    return Alumno(nombre, nota)

if __name__ == "__main__":
    alumno = crear_alumno()  
    print("\nDatos del Alumno:")
    alumno.imprimir_datos()  
    print("\nResultado de la evaluación:")
    alumno.evaluar()  
