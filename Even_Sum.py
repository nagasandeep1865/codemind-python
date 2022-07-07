n=int(input())
s=list(map(int,input().split()))
x=0
for i in s:
    if(i%2==0):
        x+=i
print(x)