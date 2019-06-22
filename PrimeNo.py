import math
num = int(input("Enter the number\t:"))
count = 0
for i in range(2,int(math.sqrt(num))+1):
    if num %i == 0:
        count +=1;
if count == 0:
    print(num," is prime")
    
else:
    print(num," is not prime")
