import random

number_of_letters = int(input("How many letters should it have?\n"))
number_of_numbers = int(input("How many numbers should it have?\n"))
number_of_symbols = int(input("How many symbols should it have?\n"))

letters = ['a','b','c','d','e']
numbers = ['0','1','2','3','4']
symbols = ['!','#','$','^','%']

passwordList = []

for i in range(number_of_letters):
    passwordList += random.choice(letters)
for i in range(number_of_symbols):
    passwordList += random.choice(symbols)
for i in range(number_of_numbers):
    passwordList += random.choice(numbers)

random.shuffle(passwordList)
password = ""

for item in passwordList:
    password+=item

print("Your password is: "+password)

