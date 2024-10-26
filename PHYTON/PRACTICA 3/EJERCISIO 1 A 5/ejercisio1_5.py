class Persona:
    # 2) (atributos privados)
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    # 1) (con acceso a atributos privados)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def print_persona(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

    # 3) 
    def es_mayor_de_edad(self):
        return self.__edad >= 18

    # 4) 
    def es_mayor_que(self, otra_persona):
        return self.__edad > otra_persona.get_edad()

    # 5)
    @staticmethod
    def get_mayor(persona1, persona2):
        if persona1.get_edad() > persona2.get_edad():
            return persona1
        else:
            return persona2

def obtener_datos_persona():
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    return Persona(nombre, edad)

if __name__ == "__main__":
    print("Datos de la Persona 1:")
    persona1 = obtener_datos_persona()

    print("\nDatos de la Persona 2:")
    persona2 = obtener_datos_persona()

    print("\nInformación de las personas ingresadas:")
    persona1.print_persona()
    persona2.print_persona()

    # Verificar quién es mayor
    mayor = Persona.get_mayor(persona1, persona2)
    print("\nLa persona de mayor edad es:")
    mayor.print_persona()

    if persona1.es_mayor_que(persona2):
        print(f"\n{persona1.get_nombre()} es mayor que {persona2.get_nombre()}.")
    else:
        print(f"\n{persona1.get_nombre()} no es mayor que {persona2.get_nombre()}.")

    if persona1.es_mayor_de_edad():
        print(f"\n{persona1.get_nombre()} es mayor de edad.")
    else:
        print(f"\n{persona1.get_nombre()} no es mayor de edad.")

    if persona2.es_mayor_de_edad():
        print(f"\n{persona2.get_nombre()} es mayor de edad.")
    else:
        print(f"\n{persona2.get_nombre()} no es mayor de edad.")
