import math
start = int(input("Enter the start point\t:"))
end = int(input("Enter the end point\t:"))
print("Prime no.s are:")
for j in range(start,end+1):
    count = 0
    for i in range(2,int(math.sqrt(j))+1):
        if j %i == 0 and j!=0 and j!=1:
            count +=1;
    if count == 0 and j!=0 and j!=1:
        print(j)
