s=input()
c=0
for i in s:
    if (i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u'):
        c+=1
print(c)