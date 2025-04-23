# Input
n, t = map(int, input().split())
queue = list(input())

# Simulate the process for t seconds
for _ in range(t):
    i = 0
    while i < n - 1:
        # Swap if "BG" is found
        if queue[i] == 'B' and queue[i + 1] == 'G':
            queue[i], queue[i + 1] = queue[i + 1], queue[i]
            i += 1  # Skip the next position to avoid rechecking
        i += 1

# Output
print("".join(queue))
