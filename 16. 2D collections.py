# Coleções 2D = estruturas compostas por outras coleções (listas, tuplas, etc.) dentro de si

# Lista de Listas
# = estrutura 2D mais comum. Permite acessar dados por índices [linha][coluna]
# EXEMPLO: matriz = [[1, 2, 3], [4, 5, 6]]
# É mutável, ordenada e aceita valores duplicados.

# Tupla de Listas
# = estrutura mista. A tupla é imutável, mas as listas internas podem ser alteradas.
# Boa para quando a estrutura geral deve permanecer constante, mas o conteúdo pode mudar.

# Lista de Tuplas
# = estrutura útil para representar dados fixos organizados (ex: coordenadas). A lista pode mudar (adicionar/remover), mas os elementos internos não.

# Dica 🗝: Use coleções 2D quando precisar representar tabelas, matrizes ou conjuntos de dados organizados em linhas e colunas.


fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0][1])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()