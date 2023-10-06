#Enter three names
name1=input("Please enter name #1:")
name2=input("Please enter name #2:")
name3=input("Please enter name #3:")

#names in order
print("Here are your names in every possible order:")
print("--------------------------------------------")

#combinations
print("1."+name1,name2,name3,sep=", ")
#com2
print("2.**"+name1,name3,name2+"**",sep="** **")
#com3
print("3."+name2,name1,name3,sep="-")
#com4
print("4."+name2,name3,name1,sep="\n")
#com5
print("5. "+name3,"   "+name2+"!","   "+name1,sep="\n")
#com6
print("6. "+"---"+name3,"   "+"------"+name1,"   "+"---------"+name2,sep="\n")
