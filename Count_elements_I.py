n,m=map(int,input().split())
s=list(map(int,input().split()))
m=list(map(int,input().split()))
k=list(set(s).intersection(m))
print(len(k))
