processes = [
    ["P0", 3, 1],
    ["P1", 5, 3],
    ["P2", 2, 2],
    ["P3", 1, 2],
    ["P4", 6, 3]
]

processes.sort(key=lambda x: x[1])

current_time = 0
results = []
execution_order = []

for p in processes:
    p_id, at, bt = p

    if current_time < at:
        current_time = at

    ct = current_time + bt
    tat = ct - at
    wt = tat - bt

    current_time = ct
    execution_order.append(p_id)
    results.append([p_id, at, bt, ct, tat, wt])

print("Execution Sequence:", " -> ".join(execution_order))
print("Process\tAT\tBT\tCT\tTAT\tWT")

total_tat = 0
total_wt = 0

for row in results:
    p_id, at, bt, ct, tat, wt = row
    total_tat += tat
    total_wt += wt
    print(f"{p_id}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

n = len(processes)
print(f"AVG TAT: {total_tat / n:.2f}")
print(f"AVG WT:  {total_wt / n:.2f}")

