n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in range(0,n):
    if(a[i]%2==0):
        c+=a[i]
    else:
        d+=a[i]
s=abs(c-d)
print(s)