valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']
# # pokemon = {
# #  'charmander':{'quantity':3,'fee':100,'types':['fire']},
# #  'squirtle':{'quantity':2,'fee':50,'types':['water']},
# #  'bulbasaur':{'quantity':5,'fee':25,'types':['grass']},
# #  'gyrados':{'quantity':1,'fee':1000,'types':['water','flying']}
# # }
def init():
    file = open("database.txt", "r")
    pokemon = {}
    txt = file.read().split("\n")
    for elem in txt:
        if elem == '':
            break
        data_ = elem.split(",")
        dict_ = {}
        dict_['quantity'] = int(data_[1])
        dict_['fee'] = int(data_[2])
        dict_['types'] = data_[3:]
        pokemon[data_[0]] = dict_
    return pokemon        


def save(pokemon):
    file = open("database.txt", "w+")
    txt = ''
    for key in pokemon.keys():
        txt += key + ',' + str(pokemon[key]['quantity']) + ',' + str(pokemon[key]['fee'])
        types = pokemon[key]['types']
        for type_ in types:
            txt += ',' + type_
        txt += '\n'
    file.write(txt)
    file.close()


if __name__ == '__main__':
    pokemon = init()



    while True:
        print("Welcome to the Pokemon Center!")
        choice = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ")
        choice = choice.lower()
        if choice == 'q':
            save(pokemon)
            print("See you next time!")
            break
        if choice == 's':
            name = input("Name of Pokemon to search for: ")
            name = name.lower()
            name_output = name[0].upper() + name[1:]
            if name not in pokemon.keys():
                print("We do not have any %s at the Pokemon Center\n"%(name_output))
            else:
                print("We have %d %s at the Pokemon Center"%(pokemon[name]['quantity'], name_output))
                fee = pokemon[name]['fee']
                print("It will cost $%s to adopt this Pokemon"%(f'{fee:,.2f}'))
                print("%s has the following types:"%name_output, end='')
                for elem in pokemon[name]['types']:
                    print(" %s"%(elem[0].upper() + elem[1:]), end='')
                print("\n")
        elif choice == 'e':
            max_fee = 0
            total_cost = 0
            min_fee = float("inf")
            for key in pokemon.keys():
                if pokemon[key]['fee'] > max_fee:
                    max_fee = pokemon[key]['fee']
                    max_name = key
                if pokemon[key]['fee'] < min_fee:
                    min_fee = pokemon[key]['fee']
                    min_name = key
                total_cost += pokemon[key]['fee'] * pokemon[key]['quantity']
            
            print("Highest priced Pokemon: %s @ $%s per Pokemon"%(max_name[0].upper() + max_name[1:], f'{max_fee:,.2f}'))
            print("Lowest priced Pokemon: %s @ $%s per Pokemon"%(min_name[0].upper() + min_name[1:], f'{min_fee:,.2f}'))

            print("Total cost to adopt all Pokemon in the Center: $%s\n"%(f'{total_cost:,.2f}'))
        elif choice == 'r':
            name = input("Enter name of Pokemon to remove: ")
            if name not in pokemon.keys():
                print("Pokemon not found, cannot remove\n")
            else:
                pokemon.pop(name)
                print("Pokemon removed\n")
        elif choice == 'a':
            name = input("Enter name of new pokemon: ")
            name = name.lower()
            if name in pokemon.keys():
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
                dict_ = {}
                dict_['quantity'] = num
                dict_['fee'] = fee
                dict_['types'] = type_list
                pokemon[name] = dict_
                print("Pokemon Added!\n")            
        elif choice == 'l':
            pokemon_names = list(pokemon.keys())
            pokemon_amounts = [pokemon[key]['quantity'] for key in pokemon.keys()]
            pokemon_adoption_fee = [pokemon[key]['fee'] for key in pokemon.keys()]

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
                for elem in pokemon[pokemon_names[i]]['types']:
                    print(" %s"%(elem[0].upper() + elem[1:]), end='')
                print("")
            print("")
        elif choice == 't':
            type_ = input("Enter Pokemon type: ").lower()
            names = []
            amounts = []
            fees = []
            types = []

            for key in pokemon.keys():
                if type_ in pokemon[key]['types']:
                    names.append(key)
                    amounts.append(pokemon[key]['quantity'])
                    fees.append(pokemon[key]['fee'])
                    types.append(pokemon[key]['types'])
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




            


