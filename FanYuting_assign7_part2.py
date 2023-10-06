import random
def ascii_shift(word, shift):
    bais = 0
    if shift == "up":
        bais = 1
    elif shift == 'down':
        bais = -1
    shift_word = ""
    for ch in word:
        if ch.isupper():
            shift_word += chr((ord(ch) - ord("A") + bais) % 26 + ord("A"))
        else:
            shift_word += ch
    return shift_word
def shift_right(word):
    if len(word) <= 1:
        return word
    else :
        return word[-1] + word[:-1]

def shift_left(word):
    if len(word) <= 1:
        return word
    else :
        return word[1:] + word[0]

def flip(word):
    if len(word) <= 1:
        return word
    index = len(word) // 2
    if len(word)%2 == 0:
        return word[index:] + word[:index]
    else:
        return word[index+1:] + word[index] + word[:index]

def add_letters(word, num):
    random_word = ""
    for ch in word:
        random_word += ch
        for i in range(num):
            x = random.randint(0, 25)
            random_word += chr(ord("A") + x)
        # print(ch, random_word)
    # print(random_word)
    return random_word

def delete_characters(word, num):
    delete_word = ""
    for i in range(0, len(word), num+1):
        delete_word += word[i]
    return delete_word

def add_padding(word, num):
    random_word = ""
    for i in range(num):
        x = random.randint(0, 25)
        random_word += chr(ord("A") + x)
    random_word += word
    for i in range(num):
        x = random.randint(0, 25)
        random_word += chr(ord("A") + x)
    return random_word

def remove_padding(word, num):
    return word[num: - num]


def swap_characters(word):
    swap_word = ""
    for i in range(0, len(word), 2):
        if i + 1 < len(word):
            swap_word += word[i+1]
        swap_word += word[i]
    return swap_word

def vowel_cycle(word, shift):
    cycle_word = ""
    dictory = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(word)):
        flag = 0
        for j in range(5):
            if word[i] == dictory[j]:
                if shift == 'up':
                    cycle_word += dictory[(j+1) %5]
                    flag = 1
                elif shift == 'down':
                    cycle_word += dictory[(j-1) %5]
                    flag = 1
                else:
                    continue
                break
        if flag == 0:
            cycle_word += word[i]
    return cycle_word

            

def part_2():
    while True:
        encoding = input("Enter an encoding pattern, 'end' to end: ")
        if encoding == 'end':
            break
        word = input("Enter a word to encode/decode: ")
        word = word.upper()
        encoding = encoding.upper()
        reversal_pattern = ""
        for chocie in encoding:
            if chocie == 'A':
                word = add_letters(word, 1)
                print("* Adding 1 letter between all characters:", word)
                reversal_pattern += 'X'
            elif chocie == 'U':
                word = ascii_shift(word, 'up')
                print("* ASCII shifting up:", word)
                reversal_pattern += 'D'

            elif chocie == 'D':
                word = ascii_shift(word, 'down')
                print("* ASCII shifting down:", word)
                reversal_pattern += 'U'

            elif chocie == 'X':
                word = delete_characters(word, 1)
                print("* Deleting 1 character:", word)
                reversal_pattern += 'A'

            elif chocie == 'L':
                word = shift_left(word)
                print("* Shifting left:", word)
                reversal_pattern += 'R'

            elif chocie == 'R':
                word = shift_right(word)
                print("* Shifting right:", word)
                reversal_pattern += 'L'

            elif chocie == 'F':
                word = flip(word)
                print("* Flipping:", word)
                reversal_pattern += 'F'

            elif chocie == 'S':
                word = swap_characters(word)
                print("* Swapping characters:", word)
                reversal_pattern += 'S'

            elif chocie == 'P':
                word = add_padding(word, 1)
                print("* Padding with 1 letter:", word)
                reversal_pattern += 'Q'

            elif chocie == 'Q':
                word = remove_padding(word, 1)
                print("* Removing padding of 1 letter:", word)
                reversal_pattern += 'P'

            elif chocie == 'V':
                word = vowel_cycle(word, 'up')
                print("* Cycling vowels up:", word)
                reversal_pattern += 'W'

            elif chocie == 'W':
                word = vowel_cycle(word, 'down')
                reversal_pattern += 'V'
                print("* Cycling vowels down:", word)
        print("Final encoding / decoding: %s"%word)
        print("Reversal pattern: %s\n"%"".join(list(reversed(reversal_pattern))))



if __name__ == '__main__':
    part_2()

# print( ascii_shift("apple", "up") ) # apple
# print( ascii_shift("APPLE", "up") ) # BQQMF
# print( ascii_shift("APPLE", "down") ) # ZOOKD
# print( ascii_shift("APPLE PIE and ZEBRAS", "up") ) # BQQMF QJF and AFCSBT
# print( ascii_shift("APPLE PIE and ZEBRAS", "down") ) # ZOOKD OHD and YDAQZR
# print( ascii_shift("APPLE PIE and ZEBRAS", "pikachu") ) # APPLE PIE and ZEBRAS
# print( ascii_shift("", "up") ) # (nothing prints, empty string)


# print(shift_right("apple")) # eappl
# print(shift_right("hello, world!")) # !hello, world
# print(shift_right("")) # (nothing prints, empty string)

# print(shift_left("apple")) # pplea
# print(shift_left("hello, world!")) # ello, world!h
# print(shift_left("")) # (nothing prints, empty string)

# print(flip("ABCDEFG")) # EFGDABC
# print(flip("123456")) # 456123
# print(flip("")) # (nothing prints, empty string)

# # define original word
# original = "HELLO!"
# # loop to demonstrate the function
# for num in range(1, 5):
#     # scramble the word using 'num' extra characters
#     scrambled = add_letters(original, num)
#     # output
#     print ("Adding", num, "random characters to", original, "->", scrambled)
# print()

# word1 = "HdeulHlHom!t"
# word2 = "HTLedklFNljioMH!bi"
# word3 = "HHHZeZrflqSflzOiosNU!jBk"
# word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"
# unscrambled1 = delete_characters(word1, 1)
# print ("Removing 1 character from", word1, "->", unscrambled1)
# unscrambled2 = delete_characters(word2, 2)
# print ("Removing 2 characters from", word2, "->", unscrambled2)
# unscrambled3 = delete_characters(word3, 3)
# print ("Removing 3 characters from", word3, "->", unscrambled3)
# unscrambled4 = delete_characters(word4, 4)
# print ("Removing 4 characters from", word4, "->", unscrambled4)

# print( add_padding('apple', 5) ) # DNNRXappleCDIVK
# print( add_padding('pear', 3) ) # RYCpearJEE
# print( add_padding('', 4) ) # PEJKQRUC
# print( add_padding('courant', 10) ) # BTXOVLESFNcourantHHNDWAXDKN
# print( remove_padding('DNNRXappleCDIVK', 5) ) # apple
# print( remove_padding('RYCpearJEE', 3) ) # pear
# print( remove_padding('PEJKQRUC', 4) ) # (empty string is returned)
# print( remove_padding('BTXOVLESFNcourantHHNDWAXDKN', 10) ) # courant

# print( swap_characters('apples') ) # palpse
# print( swap_characters('apple') ) # palpe
# print( swap_characters('XY') ) # YX
# print( swap_characters('X') ) # X
# print( swap_characters('') ) # (empty string is returned)

# # SAMPLE CODE
# print( vowel_cycle('APPLEJUICE', 'up') ) # EPPLIJAOCI
# print( vowel_cycle('APPLEJUICE', 'down') ) # UPPLAJOECA
# print( vowel_cycle('applejuice', 'down') ) # applejuice
# print( vowel_cycle('', 'up') ) # (empty string is returned)