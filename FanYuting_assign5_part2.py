import random
import time
from turtle import color

def is_red(x, y):
    if x>=50 and x<= 250 and y >= 50 and y<=250:
        if not (x>=200 and y>=200):
            return True
    return False
def is_blue(x,y):
    if x>=200 and x<= 300 and y >= 200 and y<=400:
        if not (x<=250 and y<=250):
            return True
    return False
def is_green(x, y):
    if x>=600 and x<= 750 and y >= 100 and y<=450:
        if not (x>=650  and x <= 700 and y<=400 and y>=150):
            return True
    return False
def is_black(x, y):
    if (x-450)**2+(y-200)**2 <= 100**2:
        return True
    else:
        return False
def is_yellow(x, y):
    if (x-450)**2+(y-200)**2 >= 100**2 and (x-450)**2+(y-100)**2 <= 50**2:
        return True
    else:
        return False
def is_grey(x, y):
    if x >=200 and x <= 250 and y>=200 and y<=250:
        return True
    else:
        return False
times = 0
while times == 0:
    try:
        times = int(input("Number of throws: "))
    except:
        print("Invalid, try again!")
        continue
    if times <= 0:
        print("Invalid, try again!")
        continue
    break

colors = [0,0,0,0,0,0,0] # red, blue, grey, black, yellow, green, misses
t1 = time.time()
for _ in range(times):
    x = random.randint(0, 799) + random.random()
    y = random.randint(0, 499) + random.random()
    if is_red(x, y):
        colors[0]+=1
    elif is_blue(x, y):
        colors[1]+=1
    elif is_green(x, y):
        colors[5]+=1
    elif is_black(x, y):
        colors[3]+=1
    elif is_yellow(x, y):
        colors[4]+=1
    elif is_grey(x, y):
        colors[2]+=1
    else:
        colors[6]+=1

    
t2 = time.time()
print("Total time elapsed: %.2f seconds\n"%(t2-t1))
print("Red:   %16s (%.2f"%(format(colors[0], ","), (colors[0]*100 / times)) + "%)")
print("Blue:  %16s (%.2f"%(format(colors[1], ","), colors[1]*100 / times) + "%)")
print("Grey:  %16s (%.2f"%(format(colors[2], ","), colors[2]*100 / times) + "%)")
print("Black: %16s (%.2f"%(format(colors[3], ","), colors[3]*100 / times) + "%)")
print("Yellow:%16s (%.2f"%(format(colors[4], ","), colors[4]*100 / times) + "%)")
print("Green: %16s (%.2f"%(format(colors[5], ","), colors[5]*100 / times) + "%)")
print("Misses:%16s (%.2f"%(format(colors[6], ","), colors[6]*100 / times) + "%)")

