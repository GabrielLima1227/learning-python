import random 

#print(help(random))

low = 1
high = 100

number = random.randint(low,high)

print(number)

number02 = random.random()

print(number02)

options = ("Rocks", "Paper", "Scissors")

option = random.choice(options)

print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)

print(cards)

