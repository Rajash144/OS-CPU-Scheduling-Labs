def non_preemptive_priority(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    is_completed = [False] * n

    wt = [0] * n
    tat = [0] * n

    while completed != n:
        idx = -1
        min_priority = float('inf')

        for i in range(n):
            if processes[i]["at"] <= current_time and not is_completed[i]:
                if processes[i]["priority"] < min_priority:
                    min_priority = processes[i]["priority"]
                    idx = i
                elif processes[i]["priority"] == min_priority:
                    if processes[i]["at"] < processes[idx]["at"]:
                        idx = i

        if idx != -1:
            current_time += processes[idx]["bt"]
            tat[idx] = current_time - processes[idx]["at"]
            wt[idx] = tat[idx] - processes[idx]["bt"]
            is_completed[idx] = True
            completed += 1
        else:
            current_time += 1

    print("\n--- Non-Preemptive Priority Scheduling Results ---")
    print("Process\tAT\tPriority\tBT\tWT\tTAT")
    for i in range(n):
        p = processes[i]
        print(f"{p['pid']}\t{p['at']}\t{p['priority']}\t\t{p['bt']}\t{wt[i]}\t{tat[i]}")

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print(f"Average WT: {avg_wt:.2f} (Rounded: {round(avg_wt)})")
    print(f"Average TAT: {avg_tat:.2f} (Rounded: {round(avg_tat)})")




def preemptive_priority(processes):
    n = len(processes)
    rt = [p["bt"] for p in processes]
    wt = [0] * n
    tat = [0] * n

    completed = 0
    current_time = 0

    while completed != n:
        idx = -1
        min_priority = float('inf')

        for i in range(n):
            if processes[i]["at"] <= current_time and rt[i] > 0:
                if processes[i]["priority"] < min_priority:
                    min_priority = processes[i]["priority"]
                    idx = i
                elif processes[i]["priority"] == min_priority:
                    if processes[i]["at"] < processes[idx]["at"]:
                        idx = i

        if idx != -1:
            rt[idx] -= 1

            if rt[idx] == 0:
                completed += 1
                finish_time = current_time + 1
                tat[idx] = finish_time - processes[idx]["at"]
                wt[idx] = tat[idx] - processes[idx]["bt"]

            current_time += 1
        else:
            current_time += 1

    print("\n--- Preemptive Priority Scheduling Results ---")
    print("Process\tAT\tPriority\tBT\tWT\tTAT")
    for i in range(n):
        p = processes[i]
        print(f"{p['pid']}\t{p['at']}\t{p['priority']}\t\t{p['bt']}\t{wt[i]}\t{tat[i]}")

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print(f"Average WT: {avg_wt:.2f} (Rounded: {round(avg_wt)})")
    print(f"Average TAT: {avg_tat:.2f} (Rounded: {round(avg_tat)})")


processes = [
    {"pid": "P1", "at": 0, "priority": 3, "bt": 3},
    {"pid": "P2", "at": 1, "priority": 2, "bt": 4},
    {"pid": "P3", "at": 2, "priority": 4, "bt": 6},
    {"pid": "P4", "at": 3, "priority": 6, "bt": 4},
    {"pid": "P5", "at": 5, "priority": 10, "bt": 2}
]

non_preemptive_priority(processes)
preemptive_priority(processes)

