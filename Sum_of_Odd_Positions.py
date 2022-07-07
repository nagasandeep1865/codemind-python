n=int(input())
s=list(map(int,input().split()))
a=0
for i in range(0,n):
    if(i%2!=0):
        a+=s[i]
print(a)