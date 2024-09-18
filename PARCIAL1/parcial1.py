"""
Escribir un programa en python que permita clasificar triangulos (isosceles, escaleno, equilatero, rectangulo) apartir de 3 valores flotantes o double ingresados desde el teclado.
definir y utilizar al menos una referencia de herencia que incluya encapsulamiento. 
el programa debe repetirce continuamente hasta que uno de los supuestos triangulos no lo sea.
"""
class Triangulo:

#aqui se evidencia el encapsulamiento ya que los triangulos se definen con guion bajo, esto indica que estos atributos son privados o protegidos y no deberían ser accesibles directamente desde afuera de esta clase.
    def __init__(self, lado_a, lado_b, lado_c):
        self._lado_a = lado_a
        self._lado_b = lado_b
        self._lado_c = lado_c

    def es_valido(self):
        return (self._lado_a + self._lado_b > self._lado_c and
                self._lado_a + self._lado_c > self._lado_b and
                self._lado_b + self._lado_c > self._lado_a)

#aqui se evidencia  la herencia porque en la clase triangulo se definen las propiedades y metodos y hace herencia a la clase clasificadortriangulo que optiene todo de clase triangulo
class ClasificadorTriangulo(Triangulo):
    def tipo(self):
        if not self.es_valido():
            return "No es un triángulo"
        if self._lado_a == self._lado_b == self._lado_c:
            return "Triángulo equilátero"
        elif self._lado_a == self._lado_b or self._lado_a == self._lado_c or self._lado_b == self._lado_c:
            return "Triángulo isósceles"
        else:
            return "Triángulo escaleno"

def es_rectangulo(lado_a, lado_b, lado_c):
    lados = sorted([lado_a, lado_b, lado_c])
    return lados[0]**2 + lados[1]**2 == lados[2]**2

def main():
    while True:
        try:
            lado_a = float(input("Ingresa el lado A: "))
            lado_b = float(input("Ingresa el lado B: "))
            lado_c = float(input("Ingresa el lado C: "))

            clasificador = ClasificadorTriangulo(lado_a, lado_b, lado_c)
            tipo_triangulo = clasificador.tipo()
            print(tipo_triangulo)

            if clasificador.es_valido() and es_rectangulo(lado_a, lado_b, lado_c):
                print("Además, es un triángulo rectángulo.")
            print()  # Línea en blanco para mejor legibilidad

        except ValueError:
            print("Por favor, ingresa valores numéricos válidos.")
            print()  # Línea en blanco para mejor legibilidad

if __name__ == "__main__":
    main()

