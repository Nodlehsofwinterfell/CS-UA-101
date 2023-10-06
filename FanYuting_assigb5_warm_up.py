length = 0
while True:
    length = int(input("How many prices would you like to collect? "))
    if length <= 0:
        print("Must be positive, try again\n")
        continue
    print("\nThanks, here we go!\n")
    break

data = []
while True:
    if len(data) == length:
        break
    num = int(input("Enter price #%d: "%(len(data)+1)))
    
    if num <= 0:
        print("No negative prices allowed, try again\n")
        continue
    data.append(num)

print("----Report----")
print("Total: %d"%sum(data))
print("Average: %.2f"%(sum(data)/length))