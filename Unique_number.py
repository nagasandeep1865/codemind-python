def convert(n):
    p=[int (i) for i in str (n)]
    return p
n=int(input())
d=n
l=len(str(d))
c=0
a=convert(n)
for i in range(0,l):
    for j in range(0,i):
        if a[i]==a[j]:
            c+=1
if(c==0):
    print("Unique Number")
else:
    print("Not Unique Number")
        