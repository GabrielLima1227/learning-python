# Variável = Um recipiente para um valor (texto, número inteiro, número decimal, booleano)
# Uma variável se comporta como se fosse o valor que ela contém

#Strings
first_name = "Gabriel"
food = "pizza"
email = "Gabriel@fake.com"

#f-strings
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")


#Intergers
age = 20
quantity = 3
number_of_students = 20

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {number_of_students} students")

#Float
price = 10.99 #
gpa = 3.2 
distance = 5.5

print(f"The price is {price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}Km")

#Bolean
is_student = True # A primeira letra é sempre maiúscula

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student!")
else:
    print("You are NOT a student!")

for_sale = False

if for_sale:
    print("That item is for sale!")
else:
    print("That item is NOT available!")

is_online = True

if is_online:
    print("You are online!")
else:
    print("You are offline!")