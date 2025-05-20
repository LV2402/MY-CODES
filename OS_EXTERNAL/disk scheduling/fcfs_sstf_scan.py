def fcfs(req, head):
    seek = 0
    for r in req:
        seek += abs(head - r)
        head = r
    print(f"FCFS Total Seek Time: {seek}")

def sstf(req, head):
    seek = 0
    visited = [False] * len(req)
    for _ in range(len(req)):
        idx = -1
        min_dist = float('inf')
        for j in range(len(req)):
            if not visited[j] and abs(req[j] - head) < min_dist:
                min_dist = abs(req[j] - head)
                idx = j
        visited[idx] = True
        seek += abs(head - req[idx])
        head = req[idx]
    print(f"SSTF Total Seek Time: {seek}")

def scan(req, head, disk_size):
    left = [r for r in req if r < head]
    right = [r for r in req if r >= head]
    left.sort()
    right.sort()
    seek=abs(head - (disk_size - 1)) + abs((disk_size-1)-left[0])

    print(f"SCAN Total Seek Time: {seek}")

# ------------------ Main ------------------ #
n = int(input("Enter number of disk requests: "))
requests = list(map(int, input("Enter the disk requests: ").split()))

if len(requests) != n:
    print("Error: Number of requests entered does not match 'n'")
    exit()

head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))

print("\n--- Disk Scheduling Results ---")
fcfs(requests, head)
sstf(requests, head)
scan(requests, head, disk_size)