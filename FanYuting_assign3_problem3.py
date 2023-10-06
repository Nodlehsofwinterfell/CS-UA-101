date=int(input("Enter a date (YYYYMMDD): "))
year=int(date/10000)

year=date//10000
month=date%10000//100
day=date%10000%100

if (year%4==0 and year%100!=0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")

if month==2:
    #check valid date
    if year<0 or month>12 or month<0 or day<0:
        print("This is not a valid date in", year)
        exit()
    if (year%4==0 and year%100!=0) or year % 400 == 0:
        if day > 29:
            print("This is not a valid date in", year)
            exit()
    else:
        if day > 28:
            print("This is not a valid date in", year)
            exit()
    #valid date, continue
            
    if day==1 or day==21:
        print("Feburary",str(day)+"st", year, "is a valid date")
    elif day==2 or day==22:
        print("Feburary",str(day)+"nd", year, "is a valid date")
    elif day==3 or day==23:
        print("Feburary",str(day)+"rd", year, "is a valid date")
    else:
        print("Feburary",str(day)+"th", year, "is a valid date")
else:
    if year==0 or month>12 or month==0 or day>31 or day==0:
        print("This is not a valid date in", year)
        exit()
    if month==1:
        if day==1 or day==21 or day==31:
            print("Janurary",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("Janurary",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("Janurary",str(day)+"rd", year, "is a valid date")
        else:
            print("Janurary",str(day)+"th", year, "is a valid date")
                    
    elif month==3:
        if day==1 or day==21 or day==31:
            print("March",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("March",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("March",str(day)+"rd", year, "is a valid date")
        else:
            print("March",str(day)+"th", year, "is a valid date")
            
    elif month==5:
        if day==1 or day==21 or day==31:
            print("May",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
             print("May",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("May",str(day)+"rd", year, "is a valid date")
        else:
            print("May",str(day)+"th", year, "is a valid date")
    elif month==7:
        if day==1 or day==21 or day==31:
            print("July",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("July",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("July",str(day)+"rd", year, "is a valid date")
        else:
            print("July",str(day)+"th", year, "is a valid date")
    elif month==8:  
        if day==1 or day==21 or day==31:
            print("August",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("August",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("August",str(day)+"rd", year, "is a valid date")
        else:
            print("August",str(day)+"th", year, "is a valid date")
    elif month==10:
        if day==1 or day==21 or day==31:
            print("October",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("October",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("October",str(day)+"rd", year, "is a valid date")
        else:
            print("October",str(day)+"th", year, "is a valid date")
    elif month==12:
        if day==1 or day==21 or day==31:
            print("December",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("December",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("December",str(day)+"rd", year, "is a valid date")
        else:
            print("December",str(day)+"th", year, "is a valid date")

    elif month==4:
        if day == 31:
            print("This is not a valid date in", year)
            exit()
        if day==1 or day==21:
            print("April",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("April",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("April",str(day)+"rd", year, "is a valid date")
        else:
            print("April",str(day)+"th", year, "is a valid date")
    elif month==6:
        if day == 31:
            print("This is not a valid date in", year)
            exit()
        if day==1 or day==21:
            print("June",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("June",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("June",str(day)+"rd", year, "is a valid date")
        else:
            print("June",str(day)+"th", year, "is a valid date")
    elif month==9:
        if day == 31:
            print("This is not a valid date in", year)
            exit()
        if day==1 or day==21:
            print("September",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("September",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("September",str(day)+"rd", year, "is a valid date")
        else:
            print("September",str(day)+"th", year, "is a valid date")
        
    elif month==11:
        if day == 31:
            print("This is not a valid date in", year)
            exit()
        if day==1 or day==21:
            print("November",str(day)+"st", year, "is a valid date")
        elif day==2 or day==22:
            print("November",str(day)+"nd", year, "is a valid date")
        elif day==3 or day==23:
            print("November",str(day)+"rd", year, "is a valid date")
        else:
            print("November",str(day)+"th", year, "is a valid date")
                


location = str.upper(input("Which hemisphere are you located in? (N)orth or (S)outh? "))
if location == 'S':
    if month == 12 or month <=2:
        print("The season on this date is SUMMER")
    elif month >=3 and month <=5:
        print("The season on this date is AUTUMN")
    elif month >= 6 and month <=8:
        print("The season on this date is WINTER")
    else :

        print("The season on this date is SPRING")

elif location == 'N':
    if month == 12 or month <=2:
        print("The season on this date is WINTER")
    elif month >=3 and month <=5:
        print("The season on this date is SPRING")
    elif month >= 6 and month <=8:
        print("The season on this date is SUMMER")
    else :

        print("The season on this date is AUTUMN")

else:
    print("Invalid entry, cannot determine season")

