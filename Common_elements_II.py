a,b=map(int,input().split())
s=list(map(int,input().split()))
x=list(map(int,input().split()))
u=[]
v=[]
p=[]
for i in s:
    if i not in u:
        u.append(i)
for j in x:
    if j not in v:
        v.append(j)
for i in u:
    if i not in v:
        p.append(i)
for j in v:
    if j not in u:
        p.append(j)
for i in p:
    print(i,end=' ')