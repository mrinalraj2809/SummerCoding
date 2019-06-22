num = int(input("Enter the number to find factorial\t:"))
fact = 1
for i in range(1,num+1):
    if num == 0:
        break
    else:
        fact = fact * i
print("Factorial of ",num, " is ",fact)
