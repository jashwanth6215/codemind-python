import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
H=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(format(H,".4f"))
