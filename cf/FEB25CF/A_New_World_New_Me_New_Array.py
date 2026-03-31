import math as m

for _ in range(int(input())):
    n,k,p=map(int,input().split())
    if n*p<abs(k):
        print("-1")
    else:
        print(m.ceil(abs(k)/p))