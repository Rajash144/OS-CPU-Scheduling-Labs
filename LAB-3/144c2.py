def solve_fcfs(processes):
    procs = sorted(processes, key=lambda x: x["at"])
    current_time = 0
    results = []

    for p in procs:
        if current_time < p["at"]:
            current_time = p["at"]
        ct = current_time + p["bt"]
        tat = ct - p["at"]
        wt = tat - p["bt"]
        current_time = ct
        results.append(
            {
                "pid": p["pid"],
                "at": p["at"],
                "bt": p["bt"],
                "ct": ct,
                "tat": tat,
                "wt": wt,
            }
        )

    return sorted(results, key=lambda x: x["pid"])


def solve_sjf(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    is_completed = [False] * n
    results = []

    while completed < n:
        idx = -1
        min_bt = float("inf")

        for i in range(n):
            if processes[i]["at"] <= current_time and not is_completed[i]:
                if processes[i]["bt"] < min_bt:
                    min_bt = processes[i]["bt"]
                    idx = i

        if idx == -1:
            current_time += 1
        else:
            p = processes[idx]
            ct = current_time + p["bt"]
            tat = ct - p["at"]
            wt = tat - p["bt"]
            current_time = ct
            is_completed[idx] = True
            completed += 1
            results.append(
                {
                    "pid": p["pid"],
                    "at": p["at"],
                    "bt": p["bt"],
                    "ct": ct,
                    "tat": tat,
                    "wt": wt,
                }
            )

    return sorted(results, key=lambda x: x["pid"])


processes = [
    {"pid": "P1", "at": 3, "bt": 3},
    {"pid": "P2", "at": 2, "bt": 5},
    {"pid": "P3", "at": 5, "bt": 4},
    {"pid": "P4", "at": 1, "bt": 3},
    {"pid": "P5", "at": 6, "bt": 2},
]

fcfs_res = solve_fcfs(processes)
sjf_res = solve_sjf(processes)

fcfs_avg_tat = sum(p["tat"] for p in fcfs_res) / len(processes)
fcfs_avg_wt = sum(p["wt"] for p in fcfs_res) / len(processes)

sjf_avg_tat = sum(p["tat"] for p in sjf_res) / len(processes)
sjf_avg_wt = sum(p["wt"] for p in sjf_res) / len(processes)

print("--- FCFS RESULT ---")
print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in fcfs_res:
    print(
        f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['ct']}\t{p['tat']}\t{p['wt']}"
    )
print(f"Average TAT: {fcfs_avg_tat:.2f}")
print(f"Average WT: {fcfs_avg_wt:.2f}\n")

print("--- SJF RESULT ---")
print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in sjf_res:
    print(
        f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['ct']}\t{p['tat']}\t{p['wt']}"
    )
print(f"Average TAT: {sjf_avg_tat:.2f}")
print(f"Average WT: {sjf_avg_wt:.2f}\n")

print("--- COMPARISON ---")
print(
    f"SJF saves {fcfs_avg_wt - sjf_avg_wt:.2f} units of average waiting time compared to FCFS."
)