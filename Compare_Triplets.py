a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0;
p=0;
h=0
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i]>b[j] and i==j):
            c=c+1;
        if(a[i]<b[j] and i==j):
            p=p+1;
        if(a[i]==b[j] and i==j):
            h=h+1;
print(c,p)            
