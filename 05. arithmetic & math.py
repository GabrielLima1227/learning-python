friends = 10 

#friends = friends + 1 (+: Soma) 
friends += 1
print(friends)

#friends = friends - 2 (-: Subtração)
friends -= 2
print(friends)

#friends = friends * 3 (*: Multiplicação)
friends *= 3
print(friends)

#friends = friends / 2 (/: Divisão Inteira)
friends /= 2
print(friends)

#friends = friends ** 2 (**: Exponenciação/Potenciação)
friends **= 2
print(friends)

remainder = friends % 2 #%: Resto da Divisão

print(remainder)

x = 3.14
y = -4
z = 5

#round(number):  Quando você passa apenas um número como argumento, a função round() arredonda esse número para o inteiro mais próximo.
# Round(number, ndigits): Quando você passa dois argumentos, number é o número a ser arredondado e ndigits é o número de casas decimais para as quais você quer arredondar.
result = round(x) 
print(result)

#abs(): O valor absoluto de um número é a sua distância de zero na reta numérica, sempre um valor não negativo.
# Em resumo, abs() simplesmente remove o sinal negativo de um número (se houver) e retorna o valor positivo correspondente. Se o número já for positivo ou zero, ele é retornado sem alterações.
result = abs(y)
print(result)

#pow() é usada para calcular a potência de um número. Ela pode ser usada de duas maneiras:
#pow(base, exponent): Com dois argumentos, base é o número que será elevado à potência, e exponent é o expoente.
#pow(base, exponent, modulus): Com três argumentos, calcula (base ** exponent) % modulus. Essa forma é mais eficiente para cálculos de exponenciação modular, especialmente com números grandes, pois realiza as operações de módulo intermediariamente.
result = pow(z,2)
print(result)

#max(): É usada para retornar o maior item em um iterável (como uma lista, tupla, string, etc.) ou o maior de dois ou mais argumentos que você passar para ela.
result = max(x,y,z)
print(result)

#min(): Retorna o menor item em um iterável ou o menor de dois ou mais argumentos que você passar para ela.
result = min(x,y,z)
print(result)

import math 

#math.pi: Representa o valor da famosa constante matemática π (pi).
print(math.pi)

#math.e: Representa o valor da base do logaritmo natural, também conhecido como o número de Euler.
print(math.e)

#math.sqrt: Usada para calcular a raiz quadrada de um número.
result = math.sqrt(x)
print(result)

#math.ceil(): É usada para retornar o menor inteiro maior ou igual ao número fornecido. Em outras palavras, ela arredonda um número para o próximo inteiro para cima.
result = math.ceil(x)
print(result)

#math.floor(): Retorna o maior inteiro menor ou igual ao número fornecido. Em outras palavras, ela arredonda um número para o próximo inteiro para baixo.
result = math.floor(x)
print(result)

#Exercise01: radius

radius = float(input('Enter the radius of a circle: '))
circumference = 2 * math.pi * radius
print(f"The circumference is: {circumference, 2}cm")

#Exercise02: Areas of the circle

radius = float(input("Enter the radius of a circle: "))
area= math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm²")

#Exercise03: The hypotenuse of a triangle

a= float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")