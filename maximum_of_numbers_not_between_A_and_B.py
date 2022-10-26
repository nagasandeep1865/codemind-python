n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
p=0
for i in x:
    if i not in range(a,b+1):
        s.append(i)
        p=1
if(p==1):
    print(max(s))
else:
    print("-1")