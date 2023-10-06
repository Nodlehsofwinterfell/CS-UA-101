import random

rand1=random.randint(1,10)
rand2=random.randint(1,10)
ans=str.upper(input("What type of problem(Addition, Subtraction, Multiplication, or Random) do you want to try?"))
if ans=="ADDITION":
    print("Selection saved - ADDITION")
    operator="+"
    print("Operator to use:",operator)
    answer=rand1+rand2
elif ans=="SUBTRACTION":
    print("Selection saved - SUBTRACTION")
    operator="-"
    print("Operator to use:",operator)
    answer=rand1-rand2
elif ans=="MULTIPLICATION":
    print("Selection saved - MULTIPLICATION")
    operator="*"
    print("Operator to use:",operator)
    answer=rand1*rand2
elif ans=="RANDOM":
    chance=random.randint(1,3)
    if chance==1:
        print("... we selected ADDITION as your random problem type")
        operator="+"
        print("Operator to use:",operator)
        answer=rand1+rand2
    elif chance==2:
        print("... we selected SUBTRACTION as your random problem type")
        operator="-"
        print("Operator to use:",operator)
        answer=rand1-rand2
    elif chance==3:
        print("... we selected MULTIPLICATION as your random problem type")
        operator="*"
        print("Operator to use:",operator)
        answer=rand1*rand2
else:
    print("Invalid problem choice,game will end now.")
    exit()

problem=str(rand1)+" "+operator+" "+str(rand2)
print("")
print("Guess 1")
print("What is"+" "+problem+" "+"?")
result=int(input("What is your answer?"))
if result==answer:
    print("You answered correctly!")
elif result!=answer:
    print("You did not answer correctly on your first try.")
    if result<answer:
        print("Your answer was too low. Try a higher number next time.")
    elif result>answer:
        print("Your answer was too high. Try a lower number next time.")
    print("")
    print("Guess 2")
    print("What is"+" "+problem+" "+"?")
    result=int(input("What is your answer?"))
    if result==answer:
        print("You answered correctly on your second try!")
    elif result!=answer:
        print("You did not answer correctly on your second try.")
    if result<answer:
        print("Your answer was too low. Try a higher number next time.")
    elif result>answer:
        print("Your answer was too high. Try a lower number next time.")
        print("")
        print("Guess 3")
        print("What is"+" "+problem+" "+"?")
        result=int(input("What is your answer?"))
        if result==answer:
            print("You answered correctly on your third try!")
        elif result!=answer:
            print("You did not answer correctly on your third try.")


    

