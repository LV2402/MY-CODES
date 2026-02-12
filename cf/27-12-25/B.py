for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    total = 0
    mn = 10**30
    for x in a:
        ax = abs(x)
        total += ax
        mn = min(mn, ax)

    print(total - mn)
