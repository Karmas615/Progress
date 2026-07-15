#list methods
numbers = [1, 2, 3, 3, 3, 5, 6, 7, 8, 9]
list2 = []
for number in numbers:
    if number not in list2:
        list2.append(number)
print(list2)

#dictionary
phone = input("Enter your phone number: ")
digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for num in phone:
    output += digits.get(num, "!") + " "
print(output)

#Emoji converter
message = input("Please enter your message: ")
words = message.split(" ")
dictionary = {
    ":)": "😊",
    ":(": "😞"
}
output = ""
for word in words:
    output += dictionary.get(word, word) + " "
print(output)

#function
def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
    print("welcome")

print("Start")
greet_user("John", "Smith")
greet_user("Mary", "Jane")
print("Finish")

#Function calculator
def calculator(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
result = calculator(x, y, op)
print(f"The result of {x} {op} {y} is: {result}")

#Function password checker
def check_password(password, min_length):
    if len(password) < min_length:
        return "Too short"
    return "Password accepted"

pwd = input("Enter a password: ")
result = check_password(pwd, 8)
print(result)
