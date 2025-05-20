def fcfs():
    n = int(input("Enter the number of processes: "))
    processes = []
    print("Enter Process ID, Arrival Time, and Burst Time:")
    for _ in range(n):
        pid, at, bt = input().split()
        processes.append((pid, int(at), int(bt)))
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time (AT)
    ct = 0  # Completion Time
    gc = []  # Gantt Chart
    total_tat = 0  # Total Turnaround Time
    total_wt = 0   # Total Waiting Time
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for pid, at, bt in processes:
        if ct < at:  # If CPU is idle
            gc.append(("Idle", at - ct))
            ct = at
        ct += bt
        tat = ct - at  # Turnaround Time
        wt = tat - bt  # Waiting Time
        total_tat += tat
        total_wt += wt
        gc.append((pid, bt))
        print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    print("\nGantt Chart:")
    time = 0
    for pid, duration in gc:
        print(f"| {pid}\t", end="")
        time += duration
    print("|")
    time = 0
    for pid, duration in gc:
        print(f"{time}\t", end="")
        time += duration
    print(f"{time}")
    print(f"\nAverage Turnaround Time (TAT): {avg_tat:.2f}")
    print(f"Average Waiting Time (WT): {avg_wt:.2f}")
fcfs()