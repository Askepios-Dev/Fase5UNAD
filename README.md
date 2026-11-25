# Videoteca Digital - Fase 5 Evaluación Final POA

**Curso:** Fundamentos de Programación (213022)
**Universidad:** Universidad Nacional Abierta y a Distancia (UNAD)
**Estudiante:** Alejandro Rojas Higinio
**Programa académico:** Ingenieria de sistemas
**Problema desarrollado:** Problema 4

## Descripción

Programa en Python que analiza el catálogo de una videoteca digital y cuenta cuántos títulos cumplen, al mismo tiempo, dos criterios:

1. Calificación mayor o igual a un umbral definido por el usuario.
2. Año de lanzamiento mayor o igual a un año límite definido por el usuario.

## Estructura de los datos

El catálogo es una matriz (lista de listas) con 7 títulos. Cada fila tiene el formato:

```
[Título, Año de lanzamiento, Calificación (1 a 10), Género]
```

| Índice | Dato |
|--------|------|
| 0 | Título |
| 1 | Año de lanzamiento |
| 2 | Calificación |
| 3 | Género |

## Funciones

- `contar_titulos(matriz, calif_minima, anio_limite)`: recorre la matriz con un ciclo `for` y usa un contador para sumar los títulos que cumplen ambas condiciones con `and`. Devuelve el total.
- `pedir_entero(mensaje, minimo, maximo)`: pide un número entero al usuario y repite la pregunta hasta que el dato sea válido (usa `while` y `try/except`).
- `main()`: función principal que pide los datos, llama a `contar_titulos` y muestra el resultado.

## Cómo ejecutar

Requisito: tener Python 3 instalado.

```bash
python main.py
```

El programa pedirá la calificación mínima (1 a 10) y el año límite, y mostrará el total de títulos que cumplen ambos criterios.

## Ejemplos de prueba

| Calificación mínima | Año límite | Resultado esperado |
|---------------------|------------|--------------------|
| 8 | 2010 | 4 |
| 9 | 2015 | 2 |
| 10 | 2000 | 1 |
| 5 | 1990 | 7 |

## Conceptos utilizados

Variables, listas y matrices, funciones con parámetros y retorno, ciclo `for`, ciclo `while`, condicionales con operador lógico `and`, contadores y manejo de excepciones.