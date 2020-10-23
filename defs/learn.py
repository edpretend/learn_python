number1 = input("Please input the first number:")

while True:
    try:
        n1 = int(number1)
        break
    except ValueError:
        number1 = input("Please input the first number:")


number2 = input("Then input the second number:")

while True:
    try:
        n2 = int(number2)
        break
    except ValueError:
        number2 = input("Please input the second number:")

try:
    sum = n1 + n2
except NameError:
    print("We just add numbers!")
else:
    print("The sum of " + str(n1) +" and " + str(n2) + " is " + str(sum))