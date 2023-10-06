#worked with room 9
width1 = int(input("Enter the width for Rectangle #1:"))
length1 = int(input("Enter the length for Rectangle #1:"))
width2 = int(input("Enter the width for Rectangle #2:"))
length2 = int(input("Enter the length for Rectangle #2:"))

#calculation
area1 = width1 * length1
area2 = width2 * length2
print ("")
#print
print("Rectangle #1 has an area of", area1)
print("Rectangle #2 has an area of", area2)
# square or not
if width1 == length1:
    print ("Rectangle #1 is a square!")
if width2 == length2:
    print ("Rectangle #2 is a square!")
print ("")
# compare the areas
if area1 == area2:
    print ("Rectangle #1 and Rectangle #2 have the same size!")
elif area1 > area2:
    print ("Rectangle #1 is larger than Rectangle #2!")
else:
    print("Rectangle #2 is larger than Rectangle #1!")
