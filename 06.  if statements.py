# if: Execute algum código SOMENTE SE alguma condição for Verdadeira
#elif: Senão, SE outra condição for Verdadeira, execute este código
# else: Caso contrário, execute outra coisa

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sing up!")
elif age >= 18:
    print("Your are now signed up!")
elif age <= 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sing up")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

response = input("Would you like food? (Y/N): ")
if response == "Y": # ==: É um operador de comparação que verifica se dois valores são iguais. Ele compara o valor da expressão à sua esquerda com o valor da expressão à sua direita e retorna:
    print("Have some food!")
else:
    print("No food for you!")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

name =  input("Enter your name:" )
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

