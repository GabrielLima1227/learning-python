# format specifiers = {:flags} formatam um valor com base nas
# flags (sinalizadores) inseridas.

# .(número)f = arredonda para o número de casas decimais especificado (ponto fixo)
# :(número) = aloca essa quantidade de espaços
# :0(número) = aloca essa quantidade de espaços e preenche com zeros à esquerda
# :< = justificar à esquerda
# :> = justificar à direita
# :^ = centralizar
# :+ = usar um sinal de mais para indicar valores positivos
# : = = posicionar o sinal na posição mais à esquerda (apenas para números) 
# : = inserir um espaço antes de números positivos
# :, = usar separador de milhares (vírgula)

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")