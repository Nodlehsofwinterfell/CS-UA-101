def input_username():
    while True:
        username = input("Enter a username: ")
        length = len(username)
        flag = True
        upper = 0
        lower = 0
        numeric = 0
        first_digit = False
        end_digit = False
        if username[0].isdigit():
            first_digit = True
        elif username[-1].isdigit():
            end_digit = True
        for char in username:
            if char.isdigit():
                numeric += 1
            elif char.isalpha():
                if char.islower():
                    lower += 1
                else:
                    upper += 1
            else:
                flag = False
        print("* Length of username:", length)
        if length < 8 or length > 15:
            print(" ERROR - username must be between 8 and 15 characters long")
        print("* All characters are alphabetic or numeric:", flag)
        if not flag:
            print(" ERROR - characters must be alphabetic or numeric")
        print("* First character is a digit:", first_digit)
        if first_digit:
            print(" ERROR - last character cannot be a digit")
        print("* Last character is a digit:", end_digit)
        if end_digit:
            print(" ERROR - first character cannot be a digit")
        print("* # of uppercase characters:", upper)
        if upper == 0:
            print(" ERROR - username must contain at least one uppercase character")
        print("* # of lowercase characters:", lower)
        if lower == 0:
            print(" ERROR - username must contain at least one lowercase character")
        print("* # of digit characters:", numeric)
        if numeric == 0:
            print(" ERROR - username must contain at least one digit character")
        if flag and not first_digit and not end_digit and upper != 0 and lower != 0 and numeric != 0:
            print("Username is valid\n")
            break
        else:
            print("Username is not valid, please try again\n")
    return username
def input_password(username):
    while True:
        password = input("Enter a password: ")
        length = len(password)
        part_username = password in username
        upper = 0
        lower = 0
        numeric = 0
        special = 0
        invalid = 0
        for char in password:
            if char.isdigit():
                numeric += 1
            elif char.isalpha():
                if char.islower():
                    lower += 1
                else:
                    upper += 1
            elif char in "#%$!":
                special += 1

            else:
                invalid += 1
            # print(upper, lower, numeric, special, invalid)
        print("* Length of password:", length)
        if length < 8:
            print(" ERROR - password must be at least 8 characters long")
        print("* Username is part of password:", part_username)
        if part_username:
            print(" ERROR - username cannot exist within password")
        print("* # of uppercase characters in the password:", upper)
        if upper == 0:
            print(" ERROR - password must contain at least one uppercase character")
        print("* # of lowercase characters in the password:", lower)
        if lower == 0:
            print(" ERROR - password must contain at least one lowercase character")
        print("* # of digit characters in the password:", numeric)
        if numeric == 0:
            print(" ERROR - password must contain at least one digit character")
        print("* # of special characters in the password:", special)
        if special == 0:
            print(" ERROR - password must contain at least one special character")
        print("* # of invalid characters in the password:", invalid)
        if invalid != 0:
            print(" ERROR - password cannot contain any invalid characters")
        if length >= 8 and not part_username and upper != 0 and lower != 0 and numeric != 0 and invalid == 0:
            print("Password is valid!\n")
            break
        else:
            print("Password is no valid, please try again\n")
    return password

if __name__ == "__main__":
    username = input_username()
    password = input_password(username)

            
