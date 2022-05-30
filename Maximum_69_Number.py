n=int(input())
d=0
p=0
s=0
while n!=0:
    r=n%10
    n=n//10
    d=d*10+r
while d!=0:
    f=d%10
    if f==6 and s==0:
        f=9
        s+=1
    p=p*10+f
    d=d//10
print(p)
    