print("")
print("Challenge#3")
print("")

# function:   valid_date
# input:      two integer
# processing: Check whether the inputs form a valid date
# output:     True/False (boolean)


def valid_date(a,b):
    
    if a in[1,3,5,7,8,10,12] and b>=1 and b<32:
        return True
    elif a==2 and b>=1 and b<29:
        return True
    elif a in [4,6,9,11] and b>=1 and b<31:
        return True
    else:
        return False
    
        

print (valid_date(99,1)) # False
print (valid_date(1,99)) # False
print (valid_date(99,99)) # False

print (valid_date(-99,1)) # False
print (valid_date(1,-99)) # False
print (valid_date(-99,-99)) # False

print (valid_date(9,25)) #True
print (valid_date(10,15)) # True
print (valid_date(11,31)) # False
print (valid_date(2,28)) # True
print (valid_date(2,29)) # False
