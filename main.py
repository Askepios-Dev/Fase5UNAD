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

total = contar_titulos(catalogo, 8, 2010)
print("Títulos que cumplen ambos criterios:", total)