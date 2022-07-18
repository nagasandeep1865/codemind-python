a,b=map(int,input().split())
s=list(map(int,input().split()))
n=list(map(int,input().split()))
c=[]
v=[]
d=0
g=0
for i in s:
    if i not in c:
        c.append(i)
for j in n:
    if j not in v:
        v.append(j)
for i in c:
    if i not in v:
        d+=1
for i in v:
    if i not in c:
        g+=1
print(d+g)