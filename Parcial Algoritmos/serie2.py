def mostrar_mensaje(mensaje):
    print(mensaje)

def carga_suman_t():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2
    print("La suma de los dos valores es:", suma)

carga_suman_t()
mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")