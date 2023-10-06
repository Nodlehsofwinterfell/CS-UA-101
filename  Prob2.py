
P="paper"
R="rock"
S="scissor"
L="lizard"
O="spock"
import random


while True:
    print("Let's Play Rock, Paper, Scissors, Lizard, Spock!")
    win=int(input("How many wins is required to end the tournament?"))
    if win==0 or win<=0:
        print("Invalid, try again")
        continue
    if win>0:
        print("")
        print("OK, here we go")
        print("")
        print("-------------------------------------")
        print("Round #1")
        number=0
        print("The computer has won",number,"rounds")
        print("There have been",number, "ties so far")
        print("-------------------------------------")
        print("")
        print("")
        break
while True:
    ans=input("(R)ock, (P)aper, (S)cissors, (L)izard or Sp(O)ck:")
    ans1=ans.upper()
    if ans1=="R" or ans1=="P" or ans1=="S" or ans1=="L" or ans1=="O":
        ans1=ans.upper()
        print("")
        print("-------------------------------------")
        print("Round #1")
        number=0
        print("The computer has won",number,"rounds")
        print("There have been",number, "ties so far")
        print("-------------------------------------")
        print("")
        print("")
        break
    else:
        print("This is an invalid choice, please try again.")
        continue
      
while True:
    computer=random.randint(1,5)
    #1=="Rock"
    #2=="Paper"
    #3=="Scissor"
    #4=="Lizard"
    #5=="Spock"
    #print(ans1,computer)
    if computer==3 and ans1=="P":
        print("The computer has selected Scissor")
        print("Scissors cuts Paper")
        break
    if computer==1 and ans1=="P":
        print("The computer has selected Rock")
        print("Paper covers Rock")
        print("User wins!")
        break
    if computer==4 and ans1=="P":
        print("The computer has selected Lizard")
        print("Lizard eats Paper")
        break
    if computer==4 and ans1=="R":
        print("The computer has selected Lizard")
        print("Rock crushes Lizard")
        print("User wins!")
        break
    if computer==4 and ans1=="O":
        print("The computer has selected Lizard")
        print("Lizard poisons Spock")
        break
    if computer==3 and ans1=="O":
        print("The computer has selected Scissor")
        print("Spock smashes Scissors")
        print("User wins!")
        break
    if computer==3 and ans1=="L":
        print("The computer has selected Scissor")
        print("Scissors decapitates Lizard")
        break
    if computer==2 and ans1=="O":
        print("The computer has selected Paper")
        print("Paper disproves Spock")
        break
    if computer==5 and ans1=="R":
        print("The computer has selected Spock")
        print("Spock vaporizes Rock")
        break
    if computer==3 and ans1=="R":
        print("The computer has selected Spock")
        print("Rock crushes Scissors")
        print("User wins!")
        break
    if computer==3 and ans1=="R":
        print("The computer has selected Paper")
        print("Scissors cuts Paper")
        break
    if computer==3 and ans1=="R":
        print("The computer has selected Paper")
        print("Paper covers Rock")
        break
    if computer==3 and ans1=="L":
        print("The computer has selected Paper")
        print("Lizard eats Paper")
        print("User wins!")
        break
    if computer==1 and ans1=="L":
        print("The computer has selected Rock")
        print("Rock crushes Lizard")
        break
    if computer==5 and ans1=="L":
        print("The computer has selected Spock")
        print("Lizard poisons Spock")
        print("User wins!")
        break
    if computer==5 and ans1=="S":
        print("The computer has selected Spock")
        print("Spock smashes Scissors")
        break
    if computer==4 and ans1=="S":
        print("The computer has selected Lizard")
        print("Scissors decapitates Lizard")
        print("User wins!")
        break
    if computer==5 and ans1=="P":
        print("The computer has selected Spock")
        print("Paper disproves Spock")
        print("User wins!")
        break
    if computer==1 and ans1=="O":
        print("The computer has selected Rock")
        print("Spock vaporizes Rock")
        print("User wins!")
        break
    if computer==1 and ans1=="S":
        print("The computer has selected Rock")
        print("Rock crushes Scissors")
        break
