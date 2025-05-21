# Operadores de Associação: Usados para verificar se um valor ou variável está presente em uma sequência (string, lista, tupla, conjunto ou dicionário).
# Os operadores são:
# 1. in
# 2. not in

email = "BroCode@gmail.com"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")