a=int(input())
b=int(input())
n=a
m=b
s=0
l=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range(1,b):
    if b%j==0:
        l+=j
if s==m and l==n:
    print("Amicable")
else:
    print("Not Amicable")