# Range - CloneRange
# range(x) => start = 0, stop = x - 1, step = 1
# range(x, y) => start = x, stop = y - 1, step = 1
# range(x, y, z) => start = x, stop = y - 1, step = z

def clone_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = -step

    data = []
    while start < stop:
        data.append(start)
        start += step
    return data

for i in clone_range(2, 24.7, 2.4):
    print(i)
