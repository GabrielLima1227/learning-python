# dictionary = uma coleção de pares {chave: valor}
# Dicionários (Dictionaries) são ordenados e mutáveis (podem ser alterados). Não permitem chaves duplicadas.

capitals = {"USA": "Washington", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("India"))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exist")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})

print(capitals)

capitals.pop("India")
capitals.popitem()
#capitals.clear()

print(capitals.keys())
print(capitals.values())


for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

print(capitals.items())


for key, value in capitals.items():
    print(f"{key}: {value}")