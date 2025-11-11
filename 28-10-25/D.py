import math

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    g=a[0]
    
    for num in a[1:]:
        g=math.gcd(g,num)

    x=2
    while math.gcd(x, g)!=1:
        x+=1
        
    print(x)
