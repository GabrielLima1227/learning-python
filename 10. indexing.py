# Indexação = acessando elementos de uma sequência usando [] (operador de indexação)
# [início:fim:passo]

credit_number = "1234-5678-9012-3456" # Exemplo de número de cartão de crédito

# print(credit_number[0]): Acessa e imprime o primeiro caractere da string.
# Em Python, a indexação começa em 0, então [0] se refere ao primeiro elemento.
print(credit_number[0])

# print(credit_number[:4]): Acessa e imprime os caracteres do início da string até (mas não incluindo) o índice 4.
# Quando o início não é especificado, assume-se 0.
print(credit_number[:4])

# print(credit_number[5:9]): Acessa e imprime os caracteres do índice 5 até (mas não incluindo) o índice 9.
print(credit_number[5:9])

# print(credit_number[5:]): Acessa e imprime os caracteres do índice 5 até o final da string.
# Quando o fim não é especificado, assume-se o final da string.
print(credit_number[5:])

# print(credit_number[-1]): Acessa e imprime o último caractere da string.
# Índices negativos contam a partir do final da string, sendo -1 o último elemento.
print(credit_number[-1])

# print(credit_number[::3]): Acessa e imprime os caracteres da string com um "passo" de 3.
# Isso significa que ele pega o primeiro caractere, depois pula 2 e pega o terceiro, e assim por diante.
print(credit_number[::3])

# last_digits = credit_number[-4:]: Acessa e armazena os últimos 4 caracteres da string.
# O uso de índices negativos com fatiamento (slice) é útil para pegar partes do final da string.
last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}"): Usa uma f-string para formatar a saída,
# exibindo os primeiros 12 dígitos como "XXXX-XXXX-XXXX-" e concatenando os últimos 4 dígitos obtidos.
print(f"XXXX-XXXX-XXXX-{last_digits}")