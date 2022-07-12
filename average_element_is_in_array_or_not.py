n=int(input())
s=list(map(int,input().split()))
a=sum(s)//n
for i in s:
    if a in s:
        print('True')
        break
else:
    print('False')
