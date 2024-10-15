from src.logica.OperacionesMCM import OperacionesEnteros
from src.logica.FaltanParametros import FaltanParametros

def main():
    cantidad_numeros = int(input("Cantidad de números: "))
    numeros = []

    for i in range(cantidad_numeros):
        print(f"Número {i + 1:2}: ", end="", flush=True)
        numeros.append(int(input("")))

    print(f"Números = {numeros}")
    operaciones_enteros = OperacionesEnteros(numeros)

    try:
        print(f"MCM = {operaciones_enteros.calcularMCM()}")
    except FaltanParametros:
        print("Faltan parámetros para calcular el MCM.")


if __name__ == '__main__':
    main()
