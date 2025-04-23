t = int(input())
p = 0
maxp = 0

for _ in range(t):
    x, y = map(int, input().split())
    p += y - x
    maxp = max(maxp, p)

print(maxp)
