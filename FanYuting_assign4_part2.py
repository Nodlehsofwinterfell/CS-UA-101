
import random
print("Let's Play Rock, Paper, Scissors, Lizard, Spock!\n")
wins = -1
while wins <= 0:
    str = input("How many wins is required to end the tournament? ")
    try:
        wins = int(str)
    except:
        print("Invalid, try again")
        continue
    if wins<=0:
        print("Invalid, try again")
print("\nOK, here we go")
cnt = 0
win_user = 0
win_computer = 0
choice_user = [0,0,0,0,0]
choice_computer = [0,0,0,0,0]
ties = 0
choice_str = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
matrix = [[-1,-1,9,2,-1],
          [1,-1,-1,-1,7],
          [0,-1,-1,5,-1],
          [-1,6,-1,-1,3],
          [8,-1,4,-1,-1]]
strings = ["Scissors cuts Paper",
            "Paper covers Rock",
            "Rock crushes Lizard",
            "Lizard poisons Spock",
            "Spock smashes Scissors",
            "Scissors decapitates Lizard",
            "Lizard eats paper",
            "Paper disproves Spock",
            "Spock vaporizes Rock",
            "Rock crushes Scissors"]
while win_user!=wins and win_computer!=wins:
    print("\n-------------------------------------")
    print("Round #%d"%(cnt+1))
    print("You have won %d rounds"%win_user)
    print("The computer has won %d rounds"%win_computer)
    print("There have been %d ties so far"%ties)
    print("-------------------------------------\n")
    
    c1 = -1
    c2 = -1
    str = input("(R)ock, (P)aper, (S)cissors, (L)izard or Sp(O)ck: ")
    if str == 'R' or str == 'r':
        c1 = 1
    elif str == 'P' or str == 'p':
        c1 = 2
    elif str == 'S' or str == 's':
        c1 = 3
    elif str == 'L' or str == 'l':
        c1 = 4
    elif str == 'O' or str == 'o':
        c1 = 5
    if c1 not in [1,2,3,4,5]:
        print("This is an invalid choice, please try again.")
        continue
    cnt+=1

    c2 = random.randint(1,5)
    choice_computer[c2-1] += 1
    choice_user[c1-1] +=1
    print("The computer has selected %s"%choice_str[c2-1])
    if c1 == c2:
        ties+=1
        print("The round has ended in a tie! No points awarded!")
        continue
    result = matrix[c1-1][c2-1]
    if result > 0:
        print(strings[result])
        win_user+=1
        print("User wins!")
    else:
        result = matrix[c2-1][c1-1]
        print(strings[result])
        win_computer+=1
        print("Computer wins!")
if wins == win_user:
    print("User wins the game!\n")
else:
    print("Computer wins the game!\n")

print("Game summary:")
print("- %s was played %d times (User=%d; Computer=%d)"%(choice_str[0],choice_user[0]+choice_computer[0], choice_user[0], choice_computer[0]))
print("- %s was played %d times (User=%d; Computer=%d)"%(choice_str[1],choice_user[1]+choice_computer[1], choice_user[1], choice_computer[1]))
print("- %s was played %d times (User=%d; Computer=%d)"%(choice_str[2],choice_user[2]+choice_computer[2], choice_user[2], choice_computer[2]))
print("- %s was played %d times (User=%d; Computer=%d)"%(choice_str[3],choice_user[3]+choice_computer[3], choice_user[3], choice_computer[3]))
print("- %s was played %d times (User=%d; Computer=%d)"%(choice_str[4],choice_user[4]+choice_computer[4], choice_user[4], choice_computer[4]))

    
