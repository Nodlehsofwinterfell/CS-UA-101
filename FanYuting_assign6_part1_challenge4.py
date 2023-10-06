print("")
print("Challeng#4")
print("")

# write a function called 'simple_sort_version1' that accepts two values.  you can assume
# that your three values will always be the same data type (all ints, all floats or all strings).
# sort these two values in ascending order and return them in that order. 
# you may use any function that you've written so far in this assignment if you'd like to (maximum, minimum, etc)

# your function should work perfectly with the following lines of code
def simple_sort_version1(a,b):
    if a<=b:
        return(a,b)
    else:
        return(b,a)
     
a,b = simple_sort_version1(10,20)
print (a,b) # 10 20

a,b = simple_sort_version1(20,10)
print (a,b) # 10 20

a,b = simple_sort_version1(30,30)
print (a,b) # 30 30
