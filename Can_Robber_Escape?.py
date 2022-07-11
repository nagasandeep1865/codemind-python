n=int(input())
s=list(map(int,input().split()))
a=0
for i in range(0,n):
    if(s[i]%2!=0):
        a+=1
if(a<=2):
    print('YES')
else:
    print('NO')