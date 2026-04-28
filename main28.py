def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    print("You selected choice: ", choice)
    print("Enter first number: ")
    num1 = float(input())
    print("Enter second number: ")
    num2 = float(input())

    if choice == '1':
        print(num1, "+", num2, "=", addition(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtraction(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiplication(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", division(num1, num2))
    else:
        print("Invalid input")

