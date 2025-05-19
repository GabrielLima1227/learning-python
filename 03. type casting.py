# Typecasting: o processo de converter uma variável de um tipo de dado para outro
# str(), int(), float(), bool()

name = "Gabriel de Lima"
age = 20
gpa = 3.2
is_student = True

#type() é usada para determinar o tipo de um objeto.
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#int() converte um valor para o tipo inteiro.
gpa = int(gpa)
print(gpa)

#float() converte um valor para o tipo ponto flutuante (número decimal).
age = float(age)
print(age)

#str() converte um valor para o tipo string (texto).
age = str(age)
print(type(age))

#bool() converte um valor para o tipo booleano (True ou False).
name = bool(name)
print(name)