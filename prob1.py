import random

size=int(input("How many sides on your dice(4, 6, 8, 10, 12 or 20)?"))
while size!=4 and size!=6 and size!=8 and size !=10 and size!= 12 and size!=20:
    print("Invalid size, try again")
    size=int(input("How many sides on your dice(4, 6, 8, 10, 12 or 20)?"))
 
print("")
print("Thanks, here we go!")
print("")

dice1=random.randint(1,size) 
dice2=random.randint(1,size) 

rolls=0
rolls+=1
even1=dice1%2
even2=dice2%2
number = 1   
high_counter = 0
##print(even1)
##print(even2)

while True:
    dice1=random.randint(1,size) 
    dice2=random.randint(1,size)
    print(str(number)+"."+" die roll is *"+str(dice1)+"* and *"+str(dice2)+"*", end="")
    if dice1==size and dice2==size:
        high_counter += 1
        print("High!", end=" ")
    if dice1==1 and dice2==size or dice1==size and dice2==1:
        print("High/low!", end=" ")
    if even1==0 and even2==0:
        print("Even!", end=" ")
    if even1!=0 and even2!=0:
        print("Odd!", end=" ")
    if even1!=0 and even2==0 or even1==0 and even2!=0:
        print("Mixed!", end=" ") 
    if dice1+dice2==size:
        print("Sum value!", end=" ")
    if dice1==dice2-1 or dice1==dice2+1 or dice2==dice1-1 or dice2==dice1+1:
        print("Neighbor!", end=" ")
    if dice1==dice2/2 and dice2==dice2/2+1 or dice2==dice1/2 and dice1==dice1/2+1:
        print("Middle!", end=" ")
    if dice1==dice2 or dice2==dice1:
        print("Double!", end=" ")
    if dice1==1 and dice2==1:
        print("Snake eye!", end=" ")
        break
    print("")
    number += 1
print("")
print("You finally got snake eyes on roll #",number)
print("Along the way you rolled HIGH",high_counter,"time(s). (",str(float(high_counter/number)),"% of all rolls)")

