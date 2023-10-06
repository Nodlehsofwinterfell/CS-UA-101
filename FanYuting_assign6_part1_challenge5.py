print("")
print("Challeng#5")
print("")


# next, write a new function called 'simple_sort_version2' that accepts three values.  you can assume
# that your three values will always be the same data type (all ints, all floats or all strings).
# sort these values in ascending order and return them. 
# you may use any function that you've written so far in this assignment if you'd like to (simple_sort_version1, maximum, minimum, etc)

# your function should work perfectly with the following lines of code

def simple_sort_version2(a,b,c):
    if a < b:
        if b < c:
            return (a, b, c)
        else:
            if a < c:
                return (a,c,b)
            else:
                return (c,a,b)
    else:
        if c < b:
            return (c,b,a)
        else:
            if c < a:
                return (b,c,a)
            else:
                return (b,a,c)
a,b,c = simple_sort_version2(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,20)
print (a,b,c) # 20 20 30
