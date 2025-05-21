#função = Um bloco de código reutilizável
#coloque () após o nome da função para invocá-la


def happy_birthday(name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("Bro", 30)
happy_birthday("Gabriel", 20)
happy_birthday("Joe", 40)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"You bill of ${amount:.2f} is due: {due_date}")

display_invoice("Gabriel",42.35,"01/02")

#retorno = instrução usada para finalizar uma função e enviar um resultado de volta para quem a chamou.

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))