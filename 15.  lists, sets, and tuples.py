# coleção = "variável" única usada para armazenar múltiplos valores

# Listas (List)
# = [] ordenada e mutável (pode ser alterada). Permite valores duplicados.

# Conjuntos (Set)
# = {} não ordenada e imutável (não pode ser alterada diretamente após a criação), mas permite Adicionar/Remover elementos. NÃO permite valores duplicados.

# Tuplas (Tuple)
# = () ordenada e imutável (não pode ser alterada). Permite valores duplicados. GERALMENTE MAIS RÁPIDA.

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[0:3])

for fruit in fruits:
    print(fruit)

print(dir(fruits))
print(len(fruits))

print("apple" in fruits)
print("pineapple" in fruits)

fruits.append("pineapple")
print("pineapple" in fruits)

fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.sort()
#fruits.clear()

print(fruits.index("orange"))
print(fruits.count("banana"))

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

candys = {"cake", "lollipop", "chocolate", "marshmallow"}

candys.add("caramel")
candys.remove("cake")
candys.pop()
candys.clear()

minecraft = ("blaze", "enderman", "zumbi", "ender dragon")

minecraft.count("blaze")