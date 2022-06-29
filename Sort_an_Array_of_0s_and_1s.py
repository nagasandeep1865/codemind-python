n=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    if(i==0):
        print(i,end=" ")
    else:
        c=c+1
for i in range(0,c):
    print("1",end=" ")