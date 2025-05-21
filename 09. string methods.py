# input(): Esta função é usada para obter entrada de dados do usuário através do console.
# O texto dentro dos parênteses é exibido como um prompt para o usuário.
name = input("Digite seu nome completo: ")
phone_number = input("Digite seu número de telefone: ")


# len(): Retorna o número de itens (o comprimento) de um objeto.
# No caso de strings, retorna o número de caracteres.
result_len = len(name)
print(f"O comprimento do nome é: {result_len}")


# .find(): Este é um método de string que retorna o índice da primeira ocorrência da substring especificada.
# Se a substring não for encontrada, ele retorna -1.
result_find_o = name.find("o")
print(f"A primeira ocorrência de 'o' está no índice: {result_find_o}")


# .rfind(): Similar ao .find(), mas retorna o índice da ÚLTIMA ocorrência da substring especificada.
# Se a substring não for encontrada, ele retorna -1.
result_rfind_q = name.rfind("q")
print(f"A última ocorrência de 'q' está no índice: {result_rfind_q}")


# .capitalize(): Este método de string retorna uma cópia da string com seu primeiro caractere em maiúscula
# e o restante em minúscula.
name_capitalized = name.capitalize()
print(f"Nome capitalizado: {name_capitalized}")


# .upper(): Este método de string retorna uma cópia da string convertida para maiúsculas.
name_upper = name.upper()
print(f"Nome em maiúsculas: {name_upper}")

# .lower(): Este método de string retorna uma cópia da string convertida para minúsculas.
name_lower = name.lower()
print(f"Nome em minúsculas: {name_lower}")

# .isdigit(): Este método de string verifica se todos os caracteres na string são dígitos e se há pelo menos um caractere.
# Retorna True se todos forem dígitos, False caso contrário.
result_isdigit = name.isdigit()
print(f"O nome contém apenas dígitos? {result_isdigit}")

# .isalpha(): Este método de string verifica se todos os caracteres na string são letras (alfabéticos)
# e se há pelo menos um caractere.
# Retorna True se todos forem letras, False caso contrário.
result_isalpha = name.isalpha()
print(f"O nome contém apenas letras? {result_isalpha}")


# .count(): Este método de string retorna o número de vezes que uma substring específica aparece na string.
result_count_hyphen = phone_number.count("-")
print(f"Número de hífens no telefone: {result_count_hyphen}")

# .replace(): Este método de string retorna uma cópia da string onde todas as ocorrências de uma substring
# antiga são substituídas por uma nova substring.
# Aqui, todos os hífens ("-") são substituídos por uma string vazia (""), efetivamente removendo-os.
phone_number_cleaned = phone_number.replace("-", "")
print(f"Número de telefone sem hífens: {phone_number_cleaned}")

#Exercício de validação de entrada do usuário

#1. O nome de usuário não deve ter mais de 12 caracteres
#2. O nome de usuário não deve conter espaços
#3. O nome de usuário não deve conter dígitos

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")