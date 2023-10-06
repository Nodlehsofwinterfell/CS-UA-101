print("**************************************************")
print("       3 Year Bank Account Balance Forecast       ")
print("**************************************************")
print("This program will project how much you could earn by investing money in","a bank account that pays out interest on a yearly basis.",sep="\n")
print()
deposit1=float(input("To begin, enter how much money you would like to initially invest (i.e. 5000): "))
interest1=float(input("Next, enter the expected interest rate for year 1. For example, enter 5 for 5%:"))
tax1=float(input("Finally, enter the tax rate on any interest earned this year. For example, enter 15.5 for 15.5%:"))
print()
deposit2=float(input("How much will you invest at the beginning of year 2?"))
interest2=float(input("What is the expected interest rate for year 2?"))
tax2=float(input("What is the expected tax rate for interest earned in year 2?"))
print()
deposit3=float(input("How much will you invest at the beginning of year 3?"))
interest3=float(input("What is the expected interest rate for year 3?"))
tax3=float(input("What is the expected tax rate for interest earned in year 3?"))
print()
print("--- YOUR FORECAST ---")
print()
#year1 numbers
starting_balance1=0.00
interest_earned1=deposit1*(interest1/100)
tax_on_interest1=interest_earned1*(tax1/100)
total1=deposit1+interest_earned1-tax_on_interest1
#print(starting_balance1,deposit1,interest_earned1,tax_on_interest1,total1)
#year2 numbers
starting_balance2=float(total1)
interest_earned2=(starting_balance2+deposit2)*(interest2/100)
tax_on_interest2=interest_earned2*(tax2/100)
total2=starting_balance2+deposit2+interest_earned2-tax_on_interest2
#print(starting_balance2,deposit2,interest_earned2,tax_on_interest2,total2)
#year3 numbers
starting_balance3=float(total2)
interest_earned3=(starting_balance3+deposit3)*(interest3/100)
tax_on_interest3=interest_earned3*(tax3/100)
total3=starting_balance3+interest_earned3-tax_on_interest3
#print(starting_balance3,deposit3,interest_earned3,tax_on_interest3,total3)

#total
total_deposit=deposit1+deposit2+deposit3
total_interest_earned=interest_earned1+interest_earned2+interest_earned3
total_tax=tax_on_interest1+tax_on_interest2+tax_on_interest3


#printtable
print(format("Year","<20s"),format("Starting Balance",">24s"),format("Deposit",">23s"),format("Interest Earned",">23s"),format("Ending Balance",">23s"))
print(f'{1:<21}{starting_balance1:>24,.2f}{deposit1:>24,.2f}{interest_earned1:>24,.2f}{total1:>24,.2f}'.format(starting_balance1=starting_balance1, deposit1=deposit1, interest_earned1=interest_earned1, total1=total1))
print(f'{2:<21}{starting_balance2:>24,.2f}{deposit2:>24,.2f}{interest_earned2:>24,.2f}{total2:>24,.2f}'.format(starting_balance2=starting_balance2, deposit2=deposit2, interest_earned2=interest_earned2, total2=total2))
print(f'{3:<21}{starting_balance3:>24,.2f}{deposit3:>24,.2f}{interest_earned3:>24,.2f}{total3:>24,.2f}'.format(starting_balance3=starting_balance3, deposit3=deposit3, interest_earned3=interest_earned3, total3=total3))
print("\n")
print("Total Deposited: $"+format(total_deposit, ",.2f"))
print("Total Interest Earned: $"+ format(total_interest_earned, ",.2f"))
print("Total tax due: $"+ format(total_tax, ",.2f"))
