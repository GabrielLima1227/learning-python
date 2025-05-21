# Módulo = Um arquivo contendo código que você deseja incluir em seu programa.
# Use 'import' para incluir um módulo (integrado ou seu próprio).
# É útil para dividir um programa grande em arquivos separados e reutilizáveis.

import math
# import math as m
# from math import e


a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)

from modules import example

result_square = example.square(3)
result_cube = example.cube(3)
result_circumference = example.circumference(3)

print(f"Quadrado de 3: {result_square}")
print(f"Cubo de 3: {result_cube}")
print(f"Circunferência de raio 3: {result_circumference}")

print(f"Valor de pi do módulo example: {example.math.pi}") 