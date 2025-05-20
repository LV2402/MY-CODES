disk = [False] * 20

# Sequential Allocation
print("\n--- Sequential Allocation ---")
start = int(input("Start block: "))
length = int(input("Block count: "))

if start + length > len(disk) or any(disk[start:start+length]):
    print("Cannot allocate sequentially.")
else:
    for i in range(start, start + length):
        disk[i] = True
    print(f"Allocated: {start} to {start + length - 1}")
print("Disk state:", ["1" if x else "0" for x in disk])

# Indexed Allocation
print("\n--- Indexed Allocation ---")
index = int(input("Index block: "))
n = int(input("Number of data blocks: "))
blocks = list(map(int, input("Enter block numbers: ").split()))

if disk[index] or any(disk[b] for b in blocks):
    print("Cannot allocate indexed.")
else:
    disk[index] = True
    for b in blocks:
        disk[b] = True
    print(f"Allocated at index {index}: {blocks}")
print("Disk state:", ["1" if x else "0" for x in disk])

# Linked Allocation
print("\n--- Linked Allocation ---")
n = int(input("Number of blocks: "))
blocks = list(map(int, input("Enter block numbers: ").split()))

if any(disk[b] for b in blocks):
    print("Cannot allocate linked.")
else:
    for b in blocks:
        disk[b] = True
    print("Allocated:", " -> ".join(map(str, blocks)))
print("Disk state:", ["1" if x else "0" for x in disk])