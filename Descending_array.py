n=int(input())
s=list(map(int,input().split()))
for i in range(0,n-1):
    if(s[i]<=s[i+1]):
        print('no')
        break
else:
    print('yes')
