def operator(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        return num1/num2

done = False
result = None

while not done:
    if result:
        should_continue = input(f"Type 'yes' if you would you like to continue from the number {result} or 'no' would you like to end\n")
        if should_continue=="no":
            break
    else:
        print("Welcome to the calculator app!")
        number1 = input("What is the first number?\n")
    number2 = input("What is the second number?\n")
    operation = input("What is the operation?\n")
    result = operator(number1,number2,operation)
    print(f"{number1} {operation} {number2} = {result}")
    number1=result