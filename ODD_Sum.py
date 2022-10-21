n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    if i%2!=0:
        d.append(i)
print(sum(d))