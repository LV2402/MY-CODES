# ps, p, f, n = map(int, input("Enter Page Size, Pages, Frames, Addresses: ").split())
# pt = [i if i < f else -1 for i in range(p)]
# addrs = list(map(int, input("Enter Logical Addresses: ").split()))

# print("\nPage -> Frame Mapping:")
# for i in range(p):
#     print(f"Page {i} -> {'Frame ' + str(pt[i]) if pt[i] != -1 else 'Not Mapped'}")

# print("\nAddress Translation:")
# for a in addrs:
#     pg, off = a // ps, a % ps
#     if pg >= p or pt[pg] == -1:
#         print(f"Invalid address: {a}")
#     else:
#         pa = pt[pg] * ps + off
#         print(f"Logical {a} => Physical {pa}")

def priority_scheduling():
    n = int(input("Enter the number of processes: "))
    processes = []
    print("Enter Process ID, Arrival Time, Burst Time, and Priority:")
    for _ in range(n):
        pid, at, bt, pr = input().split()
        processes.append((pid, int(at), int(bt), int(pr)))
    
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time
    ready_queue = []
    gc = []  # Gantt Chart
    time = 0
    total_tat = 0
    total_wt = 0
    print("\nPID\tAT\tBT\tPriority\tCT\tTAT\tWT")
    while processes or ready_queue:
        while processes and processes[0][1] <= time:
            ready_queue.append(processes.pop(0))
        if ready_queue:
            ready_queue.sort(key=lambda x: x[3])  # Sort by Priority (lower is higher priority)
            pid, at, bt, pr = ready_queue.pop(0)
            time += bt
            ct = time
            tat = ct - at
            wt = tat - bt
            total_tat += tat
            total_wt += wt
            gc.append((pid, bt))
            print(f"{pid}\t{at}\t{bt}\t{pr}\t\t{ct}\t{tat}\t{wt}")
        else:
            next_arrival = processes[0][1]
            gc.append(("Idle", next_arrival - time))
            time = next_arrival

    avg_tat = total_tat / n
    avg_wt = total_wt / n

    print("\nGantt Chart:")
    time = 0
    for pid, dur in gc:
        print(f"| {pid} ", end="")
        time += dur
    print("|")
    time = 0
    for pid, dur in gc:
        print(f"{time}\t", end="")
        time += dur
    print(f"{time}")
    
    print(f"\nAverage Turnaround Time (TAT): {avg_tat:.2f}")
    print(f"Average Waiting Time (WT): {avg_wt:.2f}")

priority_scheduling()
