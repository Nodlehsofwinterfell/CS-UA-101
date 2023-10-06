print("Challenge#1")
print('')
# these are the basic arithmetic functions you will be using for this challenge

# function:   add
# input:      two integers/floats
# processing: adds the two supplied values
# output:     returns the sum (integer/float)
def add(a,b):
    return a+b

# function:   sub
# input:      two integers/floats
# processing: subtracts the two supplied values
# output:     returns the difference (integer/float)
def sub(a,b):
    return a-b

# function:   mult
# input:      two integers/floats
# processing: multiplies the two supplied values
# output:     returns the product (integer/float)
def mult(a,b):
    return a*b

# function:   div
# input:      two integers/floats
# processing: divides the first value by the second value
# output:     returns the result (float)
def div(a,b):
    return a/b
    
# function:   sqrt
# input:      one integer/float
# processing: computes the square root of the supplied value
# output:     returns the square root (float)
def sqrt(a):
    return a**0.5

# function:   square
# input:      one integer/float
# processing: raises the supplied integer/float to the 2nd power
# output:     returns the square (integer/float)
def square(a):
    return a**2

# translate this expression:
# x = (3-4) + (1*2)
x = add(sub(3,4),mult(1,2))
print(x) # you should expect 1 as your output

# translate this expression:
# x = 5 + 1 + 7 + 9 + 13 + 12
x = add(add(add(5,1),add(7,9)),add(13,12))
print(x) # you should expect 47 as your output

# translate this expression:
# x = (5 + 1) / (7 + 2 + 3)
x = div(add(5,1),add(add(7,2),3))
print(x) # you should expect 0.5 as your output

# compute the distance between these two points
# point 1
x1 = 0
y1 = 0

# point 2
x2 = 100
y2 = 100

distance = sqrt(add(square(sub(x2,x1)),square(sub(y2,y1))))

print (distance) # you should expect 141.4213562373095 as your output






