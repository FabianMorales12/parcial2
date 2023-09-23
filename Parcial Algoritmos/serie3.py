import sys
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_rectangulo(largo, ancho):
    return largo * ancho

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def main():
    if len(sys.argv) < 3:
        print("Uso: python programa.py figura parametros...")
        sys.exit(1)

    figura = sys.argv[1].lower()

    if figura == "circulo":
        for i, arg in enumerate(sys.argv[2:], start=1):
            radio = float(arg.split("=")[1])
            area = calcular_area_circulo(radio)
            print(f"Área circulo {i} = {area:.2f}")

    elif figura == "rectangulo":
        for i, arg in enumerate(sys.argv[2:], start=1):
            parametros = arg.split(",")
            largo = float(parametros[0].split("=")[1])
            ancho = float(parametros[1].split("=")[1])
            area = calcular_area_rectangulo(largo, ancho)
            print(f"Área rectangulo {i} = {area:.2f}")

    elif figura == "triangulo":
        # Agrega aquí la lógica para calcular el área de triángulos si es necesario.
        pass

    else:
        print("Figura no reconocida")

if __name__ == "_main_":
    main()