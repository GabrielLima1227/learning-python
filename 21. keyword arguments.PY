# argumentos por palavra-chave =  um argumento precedido por um identificador (nome do parâmetro), ajuda na legibilidade e a ordem dos argumentos não importa.
# A ordem correta dos parâmetros (na definição/chamada) é:
# 1. posicional 2. padrão (default) 3. PALAVRA-CHAVE 4. arbitrário

def hello(greeting, title, first, last):
    print(f" (greeting) (title) (first) (last)")

hello("Hello", title="Mr.", last="John", first="James")  