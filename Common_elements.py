n,m=map(int,input().split())
s=list(map(int,input().split()))
x=list(map(int,input().split()))
a=[]
b=[]
for i in s:
    if i not in a:
        a.append(i)
for j in x:
    if j not in b:
        b.append(j)
for i in a:
    for j in b:
        if(i==j):
            print(i,end=' ')