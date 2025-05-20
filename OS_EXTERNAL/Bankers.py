processes = int(input("Enter number of processes: "))
resources = int(input("Enter number of resources: "))

allocation = []
print("Enter the Allocation Matrix:")
for _ in range(processes):
    row = list(map(int, input().strip().split()))
    allocation.append(row)

max_resources = []
print("Enter the Maximum Matrix:")
for _ in range(processes):
    row = list(map(int, input().strip().split()))
    max_resources.append(row)

available = list(map(int, input("Enter the Available Resources: ").strip().split()))

# Calculate Need Matrix
need = []
for i in range(processes):
    need_row = []
    for j in range(resources):
        need_row.append(max_resources[i][j] - allocation[i][j])
    need.append(need_row)

# Display Table
print("Process\t  Allocation\t Max\t Need\t Available")
for i in range(processes):
    print(f"P{i}\t  ", end="")
    for j in range(resources):
        print(allocation[i][j], end=" ")
    print("\t ", end="")
    for j in range(resources):
        print(max_resources[i][j], end=" ")
    print("\t ", end="")
    for j in range(resources):
        print(need[i][j], end=" ")
    if i == 0:
        print("\t ", end="")
        for j in range(resources):
            print(available[j], end=" ")
    print()

# Check Safe State
finish = [False] * processes
work = available.copy()
safe_sequence = []
count = 0

print("\nChecking Safe State:")
while count < processes:
    found = False
    for i in range(processes):
        if not finish[i]:
            if all(need[i][j] <= work[j] for j in range(resources)):
                for j in range(resources):
                    work[j] += allocation[i][j]
                safe_sequence.append(i)
                finish[i] = True
                found = True
                count += 1
                print(f"P{i} executed. Available now: ", end="")
                print(' '.join(map(str, work)))
    if not found:
        print("\nSystem is in an unsafe state! Deadlock may occur.")
        exit()
print("\nSystem is in a Safe State.")
print("Safe Sequence:", end=" ")
for i in safe_sequence:
    print(f"P{i}", end=" ")
print()
print("Final Total Available Resources:", end=" ")
print(' '.join(map(str, work)))