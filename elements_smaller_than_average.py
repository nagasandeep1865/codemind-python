n=int(input())
a=list(map(int,input().split()))
c=0
l=0
for i in a:
    c+=i
s=c//n
for i in a:
    if i<=s:
        l+=1
print(l)