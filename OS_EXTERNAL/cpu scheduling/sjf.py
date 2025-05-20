def sjf():
    n = int(input("Enter the number of processes: "))
    processes = []
    print("Enter Process ID, Arrival Time, and Burst Time:")
    for _ in range(n):
        pid, at, bt = input().split()
        processes.append((pid, int(at), int(bt)))
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by Arrival Time, then Burst Time
    ready_queue = []
    gc = []  # Gantt Chart
    time = 0
    total_tat = 0
    total_wt = 0
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")    
    while processes or ready_queue:
        while processes and processes[0][1] <= time:
            ready_queue.append(processes.pop(0))
        if ready_queue:
            ready_queue.sort(key=lambda x: x[2])  # Sort ready queue by Burst Time
            pid, at, bt = ready_queue.pop(0)
            time += bt
            ct = time
            tat = ct - at
            wt = tat - bt
            total_tat += tat
            total_wt += wt
            gc.append((pid, bt))
            print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
        else:
            next_arrival = processes[0][1]
            gc.append(("Idle", next_arrival - time))
            time = next_arrival
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    print("\nGantt Chart:")
    time = 0
    for pid, duration in gc:
        print(f"| {pid} ", end="")
        time += duration
    print("|")
    time = 0
    for pid, duration in gc:
        print(f"{time}\t", end="")
        time += duration
    print(f"{time}")    
    print(f"\nAverage Turnaround Time (TAT): {avg_tat:.2f}")
    print(f"Average Waiting Time (WT): {avg_wt:.2f}")
sjf()