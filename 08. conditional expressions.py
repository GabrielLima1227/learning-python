#Expressão Condicional = Um atalho de uma linha para a instrução if-else (operador ternário)
# Imprime ou atribui um de dois valores com base em uma condição
# X se condição senão Y

num = -5
print("Positive" if num > 0 else "Negative")

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

# Expressões Condicionais (Operador Ternário)

# Verifica se 'num' é positivo ou negativo (o valor 0 é considerado False)
print("Positive" if num > 0 else "Negative ou Zero")

# Verifica se 'num' é par ou ímpar
result = "EVEN" if num % 2 == 0 else "ODD"
print(f"O número {num} é {result}")

# Encontra o maior número entre 'a' e 'b'
max_num = a if a > b else b
print(f"O maior número entre {a} e {b} é: {max_num}")

# Encontra o menor número entre 'a' e 'b'
min_num = a if a < b else b
print(f"O menor número entre {a} e {b} é: {min_num}")

# Determina o status da idade
status = "Adult" if age >= 18 else "Child"
print(f"Com {age} anos, o status é: {status}")

# Determina o clima
weather = "HOT" if temperature > 25 else "COLD" # Ajustei o limiar para HOT/COLD
print(f"Com {temperature}°C, o clima é: {weather}")

# Determina o nível de acesso com base na função do usuário
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(f"Nível de acesso para '{user_role}': {access_level}")