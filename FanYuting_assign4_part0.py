# number 1 must be positive
number1 = int(input("Number 1: "))
while number1 < 1:
    print("Invalid, try again")
    number1 = int(input("Number 1: "))


# number 2 must be positive and bigger than number 1
while True:
    number2 = int(input("Number 2: "))
    if number2 <= number1:
        print("Invalid, try again")
    else:
        break


# top half of the arrow
current_number = number1
while current_number <= number2:
    print(current_number, current_number * "*")
    current_number += 1

    
# bottom half of the arrow
current_number = number2 - 1
while current_number >= number1:
    print(current_number, current_number * "*")
    current_number -= 1
