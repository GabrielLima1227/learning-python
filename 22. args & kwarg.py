# *args = permite que você passe múltiplos argumentos não-nomeados (posicionais)
#
# **kwargs = permite que você passe múltiplos argumentos nomeados (palavra-chave)
#
# Os operadores de desempacotamento (*) e (**) são usados para isso.

# Ordem dos parâmetros na definição da função:
# 1. Posicionais
# 2. Padrão (Default)
# 3. Somente-Palavra-Chave (Keyword-Only)
# 4. ARBITRÁRIOS (*args e **kwargs)


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(7))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Fake St.", apt="100", city="Detroit", state="MI", zip="54321")


