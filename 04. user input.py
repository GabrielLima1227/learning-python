# input() Uma função que solicita ao usuário que insira dados. Retorna os dados inseridos como uma string.

name = input("What is your name?: ")
age = int(input("How old are you?: "))
age = age + 1

print(f"Hello {name}!")
print(f"HAPPY BIRTHDAY")
print(f"You are {age} years old")

#Exercise 01: Rectangle Are Calc
lenght = float(input("Enter the lenght: "))
width = float(input("Enter the width: "))
area = lenght * width

print(f"The area is: {area}cm²")

#Exercise 02: Shopping Cart Program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")