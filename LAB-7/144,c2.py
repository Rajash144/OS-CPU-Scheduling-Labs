def sstf(requests, head):
    seq = [head]
    total = 0
    reqs = requests.copy()
    curr = head
    while reqs:
        nearest = min(reqs, key=lambda x: abs(x - curr))
        total += abs(nearest - curr)
        curr = nearest
        seq.append(curr)
        reqs.remove(nearest)
    return seq, total

reqs = [3, 60, 10, 25, 30, 4]
head = 41

seq, total = sstf(reqs, head)

print("SSTF Sequence:", seq)
print("SSTF Total Movement:", total)