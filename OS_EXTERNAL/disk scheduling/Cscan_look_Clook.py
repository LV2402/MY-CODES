# Input
req = list(map(int, input("Enter requests: ").split()))
head = int(input("Enter initial head position: "))
size = int(input("Enter disk size: "))

# C-SCAN
l = sorted([x for x in req if x < head])
r = sorted([x for x in req if x >= head])
h = head
count = 0
if l:  # Check if there are elements to the left
    a = max(l)
else:
    a = 0
count = abs(h - (size - 1)) + (size - 1) + a
print("\nC-SCAN:\nTotal Seek:", count)

# LOOK
h = head
count = 0
a, b = max(req), min(req)
count = abs(h - a) + abs(b - a)
print("\nLOOK:\nTotal Seek:", count)

# C-LOOK
h = head
count = 0
if l:  # Only if left requests exist
    c, d = max(l), min(l)
else:
    c = d = 0
a, b = max(req), min(req)
count = abs(h - a) + abs(b - a) + abs(c - d)
print("\nC-LOOK:\nTotal Seek:", count)