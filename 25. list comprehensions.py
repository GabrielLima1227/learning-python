# List comprehension: Uma maneira concisa de criar listas em Python.
#
# É uma sintaxe compacta e mais fácil de ler do que os loops tradicionais.
#
# Sintaxe geral: [expressão for valor in iterável if condição]
#
# Exemplos:
# 1. Criar uma lista de números de 0 a 4:
#    numeros = [i for i in range(5)]  # Resultado: [0, 1, 2, 3, 4]
#
# 2. Criar uma lista de quadrados de números pares:
#    quadrados_pares = [x**2 for x in range(10) if x % 2 == 0] # Resultado: [0, 4, 16, 36, 64]

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[8] for fruit in fruits]
print(fruit_chars)

numbers = [1, 2, 3, 4, 5, 6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)