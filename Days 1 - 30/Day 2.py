#car game
command = ""
started = False
while True:
    command = input(">").upper()
    if command == "START":
        if started == True:
            print("Car is already started.")
        else:
            started = True
            print("Car is starting...")           
    elif command == "STOP":
        if started == False:
            print("Car is already stopped.")
        else:
            print("Car is stopping...")
            started = False
    elif command == "QUIT":
        print("Exiting the program...")
        break
    elif command == "HELP":
        print("Available commands: START, STOP, QUIT, HELP")
    else:
        print("I don't understand that command.")

#for loops
prices = [10, 20, 30, 40, 50]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

#nested loops
numbers = [1,1,1,1,1,1,1,7]
for x_count in numbers: 
    output = ""
    for count in range(x_count):
        output += 'x'
    print(output)

#list
numbers = [101,1, 2, 3, 4,100, 5,3,8,9,10]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(f"The maximum number is: {max_number}")

you are stupid


