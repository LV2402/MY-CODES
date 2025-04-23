# Input reading
n, k = map(int, input().split())
l = list(map(int, input().split()))

# Score of the k-th place participant (0-indexed)
a = l[k - 1]

# Count the number of participants with scores >= a and > 0
c = 0
for score in l:
    if score >= a and score > 0:
        c += 1

# Output the number of participants who advance
print(c)
