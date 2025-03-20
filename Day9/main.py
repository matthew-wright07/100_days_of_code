bids = {}

more_people = True
biggest = 0
person = ""

while more_people:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bids[name] = bid
    is_more = input("Is there any more people? Type 'Yes' for more type 'No' if no more\n").lower()
    if is_more == "no":
        more_people=False
    else:
        print("\n"*10)

for key in bids:
    value = bids[key]
    if value > biggest:
        biggest = value
        person = key

print(f"The winner is {person} with a bid of {biggest}.")
print(bids)
