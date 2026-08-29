processes = [
    {"pid": "P1", "at": 4, "bt": 2},
    {"pid": "P2", "at": 2, "bt": 2},
    {"pid": "P3", "at": 1, "bt": 3},
    {"pid": "P4", "at": 0, "bt": 6},
    {"pid": "P5", "at": 3, "bt": 1},
]

tq = 2

for p in processes:
    p["rt"] = p["bt"]

current_time = 0
completed = 0
n = len(processes)

while completed < n:
    available = [
        p for p in processes if p["at"] <= current_time and p["rt"] > 0
    ]

    if not available:
        current_time += 1
        continue

    available.sort(key=lambda p: (p["rt"], p["at"]))
    p = available[0]

    time_slice = min(p["rt"], tq)

    p["rt"] -= time_slice
    current_time += time_slice

    if p["rt"] == 0:
        p["ct"] = current_time
        p["tat"] = p["ct"] - p["at"]
        p["wt"] = p["tat"] - p["bt"]
        completed += 1

total_tat = sum(p["tat"] for p in processes)
total_wt = sum(p["wt"] for p in processes)

avg_tat = total_tat / n
avg_wt = total_wt / n

print(f"{'PID':<5} {'AT':<5} {'BT':<5} {'CT':<5} {'TAT':<5} {'WT':<5}")
for p in processes:
    print(
        f"{p['pid']:<5} {p['at']:<5} {p['bt']:<5} {p['ct']:<5} {p['tat']:<5} {p['wt']:<5}"
    )

print(f"\nAverage TAT: {avg_tat:.2f}")
print(f"Average WT: {avg_wt:.2f}")
