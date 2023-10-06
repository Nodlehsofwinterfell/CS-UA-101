size = -1
while size not in [4,6,8,10,12,20]:
    str = input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? ")
    try:
        size = int(str)
    except:
        print("Invalid size, try again.")
        continue
    if size not in [4,6,8,10,12,20]:
        print("Invalid size, try again.")
nums = [0 for i in range(10)]
cnt = 0
a_list = [3,4,6,3,3,2,2,3,5,4,5,1,2,5,1,1,3,1,3,5,2,1,1,1,3,5,2,4,1,3,1]
b_list = [1,1,1,3,5,5,2,6,6,2,3,2,1,6,3,3,6,5,2,2,2,5,4,3,1,3,6,6,4,4,1]
sum_a = 0
sum_b = 0
print("\nThanks, here we go!\n")
while nums[9]==0:
    a = a_list[cnt]
    b = b_list[cnt]
    sum_a += a
    sum_b += b
    print("%d. die roll is *%d* and *%d*"%(cnt+1, a, b), end = '')
    cnt+=1 
    if a==size and b==size:
        print(" High!", end='')
        nums[0]+=1
    if a+b == size+1 and (a==1 or b==1):
        print(" High / Low!", end='')
        nums[1]+=1
    if a%2 ==0 and b%2==0:
        print(" Even!", end='')
        nums[2]+=1
    if a%2 ==1 and b%2==1:
        print(" Odd!", end='')
        nums[3]+=1
    if (a%2) + (b%2)==1:
        print(" Mixed!", end='')
        nums[4]+=1
    if a+b==size:
        print(" Sum Value!", end='')
        nums[5]+=1
    if a==b-1 or b==a-1:
        print(" Neighbor!", end='')
        nums[6]+=1
    if a+b==size+1 and (a==size//2 or b==size//2):
        print(" Middle!", end='')
        nums[7]+=1
    if a==b:
        print(" Doubles!", end='')
        nums[8]+=1
    if a==1 and b==1:
        print(" Snake Eyes!", end='')
        nums[9]+=1
    print("")
print("\nYou finally got snake eyes on roll #%d"%cnt)
print("Along the way you rolled HIGH %d time(s). (%.2f"%(nums[0], nums[0]/cnt*100),"%"," of all rolls)")
print("Along the way you rolled HIGH / LOW %d time(s). (%.2f"%(nums[1], nums[1]/cnt*100),"%"," of all rolls)")
print("Along the way you rolled EVEN %d time(s). (%.2f"%(nums[2], nums[2]/cnt*100),"%"," of all rolls)")
print("Along the way you rolled ODD %d time(s). (%.2f"%(nums[3], nums[3]/cnt*100),"%"," of all rolls)")
print("Along the way you rolled MIXED %d time(s). (%.2f"%(nums[4], nums[4]/cnt*100),"%"," of all rolls)")
print("Along the way you rolled SUM VALUE %d time(s). (%.2f"%(nums[5], nums[5]/cnt*100),"%"," of all rolls)")
print("Along the way you rolled NEIGHBOR %d time(s). (%.2f"%(nums[6], nums[6]/cnt*100),"%"," of all rolls)")
print("Along the way you rolled MIDDLE %d time(s). (%.2f"%(nums[7], nums[7]/cnt*100),"%"," of all rolls)")
print("Along the way you rolled DOUBLE %d time(s). (%.2f"%(nums[8], nums[8]/cnt*100),"%"," of all rolls)")
print("Along the way you rolled SNAKE EYES %d time(s). (%.2f"%(nums[9], nums[9]/cnt*100),"%"," of all rolls)")

print("Average roll for die #1: %.2f"%(sum_a/len(a_list)))
print("Average roll for die #2: %.2f"%(sum_b/len(b_list)))
