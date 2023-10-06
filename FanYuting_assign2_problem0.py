# variable
money= float(input("How much money did you win? "))
people_splitting = int(input("How many people are splitting the winnings?" ))
tax= float(input("What is the tax rate on lottery winnings (i.e. 25 = 25%):"))
print("")
print("")
#calculation
total= money/people_splitting
tax_person = total/4
take_home = total - tax_person

#print stage
print ("In total you want $", format(money, ",.2f"), sep="")
print ("Split "+str(people_splitting)+" ways that amounts to $", format(total,".2f"))
print("Tax per person: $", format(tax_person,".2f"))
print("Take home amount per person: $",format(take_home,".2f"))
