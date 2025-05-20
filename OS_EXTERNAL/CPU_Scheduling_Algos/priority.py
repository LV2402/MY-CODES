def priority_scheduling():
    n = int(input("Enter the number of processes: "))
    processes = []
    print("Enter Process ID, Arrival Time, Burst Time, and Priority:")
    for _ in range(n):
        pid, at, bt, pr = input().split()
        processes.append((pid, int(at), int(bt), int(pr)))
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time
    ready_queue = []
    completed_processes = []
    gc = []  # Gantt Chart
    time = 0
    total_tat = 0
    total_wt = 0
    while processes or ready_queue:
        while processes and processes[0][1] <= time:
            ready_queue.append(processes.pop(0))
        if ready_queue:
            ready_queue.sort(key=lambda x: x[3])  # Sort by Priority (lower is higher)
            pid, at, bt, pr = ready_queue.pop(0)
            time += bt
            ct = time
            tat = ct - at
            wt = tat - bt
            total_tat += tat
            total_wt += wt
            completed_processes.append((pid, at, bt, pr, ct, tat, wt))
            gc.append((pid, bt))
        else:
            next_arrival = processes[0][1]
            gc.append(("Idle", next_arrival - time))
            time = next_arrival
    # Sort completed processes by Process ID (e.g., P1, P2...)
    completed_processes.sort(key=lambda x: x[0])
    print("\nPID\tAT\tBT\tPriority\tCT\tTAT\tWT")
    for p in completed_processes:
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t\t{p[4]}\t{p[5]}\t{p[6]}")
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