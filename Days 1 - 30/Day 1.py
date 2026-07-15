#age
year_born = input("What year were you born? ")
age = 2026 - int(year_born)
print("You are " + str(age) + " years old.")

#weight converter
weight = input("What is your weight? ")
unit = input("Is your weight in (K)g or (L)bs? ")
if unit == "K" or unit == "k":
    converted_weight = int(weight) * 2.20462
    print("Your weight in pounds is: " + str(converted_weight))
elif unit == "L" or unit == "l":
    converted_weight = int(weight) / 2.20462
    print("Your weight in kilograms is: " + str(converted_weight))
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")

#calculator
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
operation = input("Enter an operation (+, -, *, /,**,%): ")
if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    if y != 0:
        print(x / y)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "**":
    print(x ** y)
elif operation == "%":
    print(x % y)
else:
    print("Invalid operation. Please enter one of the following: +, -, *, /, **, %")
print("Thank you for using the calculator!")
#hello how are you are you well?

