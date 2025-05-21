# argumentos padrão = Um valor padrão para certos parâmetros

# o padrão é usado quando esse argumento é omitido
# torna suas funções mais flexíveis, reduz o número de argumentos
# 1. posicional, 2. PADRÃO, 3. palavra-chave, 4. arbitrário

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

import time

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1) # Correção: 'time.sleep' deve ser indentado dentro do loop 'for'
    print("DONE!")

count(30, 15)