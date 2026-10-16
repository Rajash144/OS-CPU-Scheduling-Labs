
pages = [1, 2, 3, 4, 2, 3, 1]
capacity = 3

# FIFO
frames = []
faults = 0

for page in pages:
    if page not in frames:
        faults += 1
        if len(frames) < capacity:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)

print("FIFO Page Faults:", faults)

# LRU
frames = []
recent = []
faults = 0

for page in pages:
    if page not in frames:
        faults += 1
        if len(frames) == capacity:
            old = recent.pop(0)
            frames.remove(old)
        frames.append(page)
    else:
        recent.remove(page)

    recent.append(page)

print("LRU Page Faults:", faults)
