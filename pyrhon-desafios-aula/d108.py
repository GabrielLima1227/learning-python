from modulo_d108 import moeda

preco = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(preco)} e {moeda.moeda(moeda.metade(preco))}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
print(f"Aumento de 10%, temos {moeda.moeda(moeda.aumentar(preco,10))}")
