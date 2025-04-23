# Input
n = int(input())  # Number of rooms
count = 0  # Count of rooms with space for both George and Alex

for _ in range(n):
    p, q = map(int, input().split())  # Current occupants and capacity
    if q - p >= 2:  # Room has space for at least two people
        count += 1

# Output
print(count)
