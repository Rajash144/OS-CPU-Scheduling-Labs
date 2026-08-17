def fcfs(processes):
    procs = sorted(processes, key=lambda x: x["at"])
    curr_time = 0
    res = []
    for p in procs:
        if curr_time < p["at"]:
            curr_time = p["at"]
        ct = curr_time + p["bt"]
        tat = ct - p["at"]
        wt = tat - p["bt"]
        curr_time = ct
        res.append(
            {"pid": p["pid"], "at": p["at"], "bt": p["bt"], "ct": ct, "tat": tat, "wt": wt}
        )
    return sorted(res, key=lambda x: x["pid"])


def sjf(processes):
    n = len(processes)
    completed = 0
    curr_time = 0
    done = [False] * n
    res = []
    while completed < n:
        idx = -1
        min_bt = float("inf")
        for i in range(n):
            if processes[i]["at"] <= curr_time and not done[i]:
                if processes[i]["bt"] < min_bt:
                    min_bt = processes[i]["bt"]
                    idx = i
        if idx == -1:
            curr_time += 1
        else:
            p = processes[idx]
            ct = curr_time + p["bt"]
            tat = ct - p["at"]
            wt = tat - p["bt"]
            curr_time = ct
            done[idx] = True
            completed += 1
            res.append(
                {"pid": p["pid"], "at": p["at"], "bt": p["bt"], "ct": ct, "tat": tat, "wt": wt}
            )
    return sorted(res, key=lambda x: x["pid"])


def round_robin(processes, tq):
    n = len(processes)
    rem_bt = [p["bt"] for p in processes]
    ct = [0] * n
    curr_time = 0
    queue = []
    visited = [False] * n

    procs = sorted(range(n), key=lambda x: processes[x]["at"])

    curr_time = processes[procs[0]]["at"]
    queue.append(procs[0])
    visited[procs[0]] = True

    completed = 0
    while queue:
        i = queue.pop(0)

        if rem_bt[i] > tq:
            curr_time += tq
            rem_bt[i] -= tq
        else:
            curr_time += rem_bt[i]
            rem_bt[i] = 0
            ct[i] = curr_time
            completed += 1

        for j in range(n):
            if processes[j]["at"] <= curr_time and not visited[j]:
                queue.append(j)
                visited[j] = True

        if rem_bt[i] > 0:
            queue.append(i)

        if not queue and completed < n:
            for j in range(n):
                if not visited[j]:
                    curr_time = processes[j]["at"]
                    queue.append(j)
                    visited[j] = True
                    break

    res = []
    for i in range(n):
        tat = ct[i] - processes[i]["at"]
        wt = tat - processes[i]["bt"]
        res.append(
            {
                "pid": processes[i]["pid"],
                "at": processes[i]["at"],
                "bt": processes[i]["bt"],
                "ct": ct[i],
                "tat": tat,
                "wt": wt,
            }
        )
    return res


processes = [
    {"pid": "P1", "at": 0, "bt": 7},
    {"pid": "P2", "at": 1, "bt": 4},
    {"pid": "P3", "at": 2, "bt": 15},
    {"pid": "P4", "at": 3, "bt": 11},
    {"pid": "P5", "at": 4, "bt": 20},
    {"pid": "P6", "at": 4, "bt": 9},
]

fcfs_out = fcfs(processes)
sjf_out = sjf(processes)
rr_out = round_robin(processes, 5)


def print_table(title, data):
    print(f"=== {title} ===")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in data:
        print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['ct']}\t{p['tat']}\t{p['wt']}")
    avg_tat = sum(p["tat"] for p in data) / len(data)
    avg_wt = sum(p["wt"] for p in data) / len(data)
    print(f"Avg TAT: {avg_tat:.2f} | Avg WT: {avg_wt:.2f}\n")


print_table("FCFS", fcfs_out)
print_table("SJF", sjf_out)
print_table("Round Robin (TQ=5)", rr_out)

