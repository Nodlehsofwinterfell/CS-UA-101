num1=int(input("Enter a 3 digit number between 000 and 999:"))
num2=int(input("Enter a 3 digit number between 000 and 999:"))
print()
print()
#numbers
hun1=num1//100
ten1=num1//10%10
one1=num1%100
hun2=num2//100
ten2=num2//10%10
one2=num2%100
hun=hun1+hun2
ten=ten1+ten2
one=one1+one2
print("Digits in the 1's places:   ",one1,one2)
print("Digits in the 10's places:   ",ten1,ten2)
print("Digits in the 100's places:   ",hun1,hun2)
print()
print("Graphical representation of your numbers")
print()
print("Hundreds  Tens      Ones")
print("                    "+str(one1)*7)
print(str(hun2)*9,"          "+str(one2)*8)
#step2=str(hun)+str(ten)+str(one)
#step3=str(hun1)+str(ten1)+str(one1)
#step4=str(hun2)+str(ten2)+str(one2)
step2=str(hun)+str(ten)+str(one)
step3=hun1+ten1+one1
step4=hun2+ten2+one2
stepthree=str(step3)
stepfour=str(step4)
print("Computing Your Super Number!")
print()
print("Step #1: Add Each Place Value")
print("- Hundreds:","hun1","+","hun2","=",hun)
print("- Tens:    ","ten1","+","ten2","=",ten)
print("- Ones:    ","one1","+","one2","=",one)
print()
print("Step #2: Combine New Values")
print("-",hun,"+",ten,"+",one,"=",step2)
print()
print("Step #3: Compute The Sum of All Digits in First Number")
print("-",hun1,"+",ten1,"+",one1,"=",int(step3))
print()
print("Step #4: Compute The Sum of All Digits in Second Number")
print("-",hun2,"+",ten2,"+",one2,"=",int(step4))
print()
print("Step #5: Combine The Numbers In This Order -- Step 3 + Step 2 + Step 4")
print("-",stepthree+step2+stepfour)
