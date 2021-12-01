import queue

q = queue.Queue()


def loadData():
    with open('data', 'r') as data:
        lines = [int(line) for line in data.readlines()]
    return lines


def increases(d):
    line = 0
    depth_current = 0
    depth = 0
    inc = -1
    while line <= len(d) - 3:
        for value in range(line, line + 3):
            depth_current += d[value]
        line += 1
        if depth_current > depth:
            inc += 1
        depth = depth_current
        depth_current = 0
    return inc


if __name__ == "__main__":
    d = loadData()
    print("Increses: ", increases(d))
