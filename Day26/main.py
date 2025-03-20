import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_data = {row["letter"]:row["code"] for (index,row) in data.iterrows()}

user_input = input("Please Choose A Word\n").upper()

letters = [letter for letter in user_input]
response = [new_data[letter] for letter in letters if letter in new_data]

print(response)
