n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    v=a.pop()
    if v==1:
        c+=pow(2,i)
print(c)