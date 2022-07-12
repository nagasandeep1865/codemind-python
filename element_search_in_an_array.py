n=int(input())
s=list(map(int,input().split()))
a=int(input())
for i in s:
    if a in s:
        print('True')
        break
else:
    print('False')