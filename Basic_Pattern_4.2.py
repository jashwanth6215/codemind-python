a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        if i%2!=0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
