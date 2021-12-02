def loaddata():
    with open("data", "r") as data:
        line = [l.split() for l in data.readlines()]
        return line


def calculate(d):
    distance = 0
    depth = 0
    aim = 0
    for e in d:
        if e[0] == 'forward':
            distance += int(e[1])
            x = int(e[1]) * aim
            depth += x
        if e[0] == 'down':
            aim += int(e[1])
        if e[0] == 'up':
            aim -= int(e[1])
        print("Distance: ", distance, "Depth: ", depth)
        print("Result: ", distance * depth)


if __name__ == "__main__":
    d = loaddata()
    calculate(d)
