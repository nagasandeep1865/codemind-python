def fact(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
a=input()
x=[]
y=[]
f=0
for i in range(0,len(a)):
    if a[i]!=',':
        x.append(int(a[i]))
for i in range(0,len(x)):
    z=fact(x[i])
    if z in x:
        f=1
        y.append(x[i])
if(f==0):
    print('-1')
else:
    b=set(y)
    print(*b)