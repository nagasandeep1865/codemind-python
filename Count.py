n=int(input())
a=list(map(int,input().split()))
c=0
p=0
for i in range(len(a)):
    if(a[i]%2==0):
        c=c+1
    if(a[i]%2!=0):
        p=p+1
print(c,p)        