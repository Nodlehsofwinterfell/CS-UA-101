pokemon_names = ['charmander', 'squirtle', 'bulbasaur', 'gyrados']
pokemon_amounts = [3, 2, 5, 1]
pokemon_types = [['fire'], ['water'], ['grass'], ['water', 'flying']]
pokemon_adoption_fee = [100.00, 50.00, 25.00, 1000.00]
while True:
    print("Welcome to the Pokemon Center!")
    choice = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ")
    choice = choice.lower()
    if choice == 'q':
        print("See you next time!")
        break
    if choice == 's':
        name = input("Name of Pokemon to search for: ")
        name = name.lower()
        name_output = name[0].upper() + name[1:]
        flag = 0
        for i in range(len(pokemon_names)):
            if pokemon_names[i] == name:
                print("We have %d %s at the Pokemon Center"%(pokemon_amounts[i], name_output))
                print("It will cost $%s to adopt this Pokemon"%(f'{pokemon_adoption_fee[i]:,.2f}'))
                print("%s has the following types:"%pokemon_names[i], end='')
                for elem in pokemon_types[i]:
                    print(" %s"%(elem[0].upper() + elem[1:]), end='')
                print("\n")
                flag = 1
                break
        if flag == 0:
            print("We do not have any %s at the Pokemon Center\n"%(name_output))
    elif choice == 'e':
        max_fee = max(pokemon_adoption_fee)
        min_fee = min(pokemon_adoption_fee)
        for i in range(len(pokemon_names)):
            if max_fee == pokemon_adoption_fee[i]:
                print("Highest priced Pokemon: %s @ $%s per Pokemon"%(pokemon_names[i][0].upper() + pokemon_names[i][1:], f'{pokemon_adoption_fee[i]:,.2f}'))
                break
        for i in range(len(pokemon_names)):
            if min_fee == pokemon_adoption_fee[i]:
                print("Lowest priced Pokemon: %s @ $%s per Pokemon"%(pokemon_names[i][0].upper() + pokemon_names[i][1:], f'{pokemon_adoption_fee[i]:,.2f}'))
                break
        total_cost = sum([pokemon_amounts[i] * pokemon_adoption_fee[i] for i in range(len(pokemon_adoption_fee))])
        print("Total cost to adopt all Pokemon in the Center: $%s\n"%(f'{total_cost:,.2f}'))
    elif choice == 'r':
        name = input("Enter name of Pokemon to remove: ")
        name = name.lower()
        flag = 0
        for i in range(len(pokemon_names)):
            if name == pokemon_names[i]:
                pokemon_names.pop(i)
                pokemon_adoption_fee.pop(i)
                pokemon_amounts.pop(i)
                pokemon_types.pop(i)
                flag = 1
                print("Pokemon removed\n")
                break
        if flag == 0:
            print("Pokemon not found, cannot remove\n")
    elif choice == 'a':
        name = input("Enter name of new pokemon: ")
        name = name.lower()
        if name in pokemon_names:
            print("Duplicate name, add operation cancelled\n")
        else:
            while True:
                num = input("How many of these Pokemon are you adding? ")
                if not num.isdigit():
                    print("Invalid, please try again")
                    continue
                num = int(num)
                if num == 0:
                    print("Invalid, please try again")
                    continue
                break
            while True:
                fee = input("What is the adoption fee for this Pokemon? ")
                try:
                    fee = float(fee)
                    if fee <= 0:
                        print("Invalid, please try again")
                    else:
                        break
                except:
                    print("Invalid, please try again")
            print("Next you will be prompted to enter the \'types\' for this Pokemon. Pokemon can have multiple types. Type \'help\' to view all possible Pokemon types, and type \'end\' to stop entering types. You must enter at least one valid \'type\'")
            type_list = []
            valid_type = "bug\n* dark\n* dragon\n* electric\n* fairy\n* fighting\n* fire\n* flying\n* ghost\n* grass\n* ground\n* ice\n* normal\n* poison\n* psychic\n* rock\n* steel\n* water".split("\n* ")
            while True:
                type_tmp = input("What type of Pokemon is this? ").lower()
                if type_tmp == 'help':
                    print("* bug\n* dark\n* dragon\n* electric\n* fairy\n* fighting\n* fire\n* flying\n* ghost\n* grass\n* ground\n* ice\n* normal\n* poison\n* psychic\n* rock\n* steel\n* water")
                elif type_tmp == 'end':
                    break
                elif type_tmp not in valid_type:
                    print("This is not a valid type, please try again")
                    continue
                else :
                    print("Type %s added"%type_tmp)
                    type_list.append(type_tmp)
            pokemon_types.append(type_list)
            pokemon_names.append(name)
            pokemon_adoption_fee.append(fee)
            pokemon_amounts.append(num)
            print("Pokemon Added!\n")            
    elif choice == 'l':
        length_1 = max(max([len(elem) for elem in pokemon_names]) + 1, 5)
        length_2 = max(max([len(str(f'{elem:,d}')) for elem in pokemon_amounts]) + 1, 20)
        length_3 = max(max([len(str(f'{elem:,.2f}')) for elem in pokemon_adoption_fee]) + 1, 15)
        # print(length_1, length_2, length_3)
        print("Name%s"%(" "*(length_1 - 4)), end='')
        print("%sAmount Available"%(" "*(length_2 - 16)), end='')
        print("%sAdoption Fee"%(" "*(length_3 - 12)), end='')
        print(" Type(s)")
        for i in range(len(pokemon_names)):
            name = pokemon_names[i]
            name = name[0].upper() + name[1:]
            print("%s%s"%(name, " " *(length_1 - len(name))), end = '')
            amount = pokemon_amounts[i]
            amount = str(f'{amount:,d}')
            print("%s%s"%(" "* (length_2 - len(amount)), amount), end = '')
            fee = pokemon_adoption_fee[i]
            fee = str(f'{fee:,.2f}')
            print("%s%s"%(" "* (length_3 - len(fee)), fee), end = '')
            for elem in pokemon_types[i]:
                print(" %s"%(elem[0].upper() + elem[1:]), end='')
            print("")
        print("")
    elif choice == 't':
        type_ = input("Enter Pokemon type: ").lower()
        names = []
        amounts = []
        fees = []
        types = []

        for i in range(len(pokemon_names)):
            if type_ in pokemon_types[i]:
                names.append(pokemon_names[i])
                amounts.append(pokemon_amounts[i])
                fees.append(pokemon_adoption_fee[i])
                types.append(pokemon_types[i])
        if len(names) == 0:
            print("We have no Pokemon of that type at our Pokemon Center\n")
        else:
            length_1 = max(max([len(elem) for elem in names]) + 1, 5)
            length_2 = max(max([len(str(f'{elem:,d}')) for elem in amounts]) + 1, 20)
            length_3 = max(max([len(str(f'{elem:,.2f}')) for elem in fees]) + 1, 15)
            # print(length_1, length_2, length_3)
            print("Name%s"%(" "*(length_1 - 4)), end='')
            print("%sAmount Available"%(" "*(length_2 - 16)), end='')
            print("%sAdoption Fee"%(" "*(length_3 - 12)), end='')
            print(" Type(s)")
            for i in range(len(names)):
                name = names[i]
                name = name[0].upper() + name[1:]
                print("%s%s"%(name, " " *(length_1 - len(name))), end = '')
                amount = amounts[i]
                amount = str(f'{amount:,d}')
                print("%s%s"%(" "* (length_2 - len(amount)), amount), end = '')
                fee = fees[i]
                fee = str(f'{fee:,.2f}')
                print("%s%s"%(" "* (length_3 - len(fee)), fee), end = '')
                for elem in types[i]:
                    print(" %s"%(elem[0].upper() + elem[1:]), end='')
                print("")
            print("")




        


