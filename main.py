catalogo = [
    ["Inception", 2010, 9, "Ciencia ficción"],
    ["Titanic", 1997, 8, "Romance"],
    ["Joker", 2019, 9, "Drama"],
    ["Shrek", 2001, 7, "Animación"],
    ["Interestelar", 2014, 10, "Ciencia ficción"],
    ["Cars", 2006, 6, "Animación"],
    ["Oppenheimer", 2023, 9, "Biografía"]
]


def contar_titulos(matriz, calif_minima, anio_limite):
    contador = 0
    for pelicula in matriz:
        if pelicula[2] >= calif_minima and pelicula[1] >= anio_limite:
            contador += 1
    return contador


def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print("Error: el valor debe estar entre", minimo, "y", maximo)
        except ValueError:
            print("Error: debe escribir un número entero.")


def main():
    umbral = pedir_entero("Ingrese la calificación mínima (1 a 10): ", 1, 10)
    anio = pedir_entero("Ingrese el año límite: ", 1900, 2026)

    total = contar_titulos(catalogo, umbral, anio)
    print("Títulos que cumplen ambos criterios:", total)


main()