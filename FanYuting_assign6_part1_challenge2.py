print("")
print("Challenge#2")
print("")
a = 5
b = 10
c = 15
d = 20
e = 20
#Function:   minimum
#Input:      two integers/floats
#Processing: pick out the lower value between inputs (integer/float)
#Output:     return the the lower value between two inputs (integer/float)
    

def minimum(x1,x2):
    
    if x1<x2:
        minimum=x1
    else:
        minimum=x2
    return minimum
#Function:   maximum
#Input:      two integers/floats
#Processing: pick out the higher value between two inputs (integer/float)
#Output:     return the the higher value between two inputs (integer/float)
def maximum (x,y):

def maximum(x1,x2):
    
    if x1>x2:
        maximum=x1
    else:
        maximum=x2
    return maximum

ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print (ans1,ans2,ans3) # 10 15 20

ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6) # 15 10 5

ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)

ans8 = maximum(d,e) # d and e are the same, so either is considered the maximum
ans8 = minimum(d,e) # d and e are the same, so either is considered the minimum
print(ans8, ans8) # 20 20

