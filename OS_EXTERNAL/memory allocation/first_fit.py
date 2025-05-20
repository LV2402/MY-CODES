def first_fit(block_sizes, m, process_sizes, n):
    allocation = [-1] * n  # Initialize allocations with -1
    for i in range(n):
        for j in range(m):
            if block_sizes[j] >= process_sizes[i] and allocation[i] == -1:
                allocation[i] = j
                block_sizes[j] = -1  # Mark block as allocated
                break

    print("Process No.\tProcess Size\tBlock No.")
    for i in range(n):
        if allocation[i] != -1:
            print(f"P{i + 1}\t\t{process_sizes[i]}\t\tB{allocation[i] + 1}")
        else:
            print(f"P{i + 1}\t\t{process_sizes[i]}\t\tNot Allocated")


# Input outside the function
m = int(input("Enter the number of blocks: "))
block_sizes = list(map(int, input("Enter the block sizes: ").split()))
n = int(input("Enter the number of processes: "))
process_sizes = list(map(int, input("Enter the process sizes: ").split()))

first_fit(block_sizes, m, process_sizes, n)