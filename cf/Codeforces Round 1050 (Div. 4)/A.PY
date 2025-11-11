for _ in range(int(input())):
    x,n=map(int,input().split())
    if n%2==0:
        print(x-x)
    else:
        print(x)