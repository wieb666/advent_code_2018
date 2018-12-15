def main(input_file):
    lines = [line.strip() for line in open(input_file)]
    x = [int(x.split(",")[0]) for x in lines]
    y = [int(y.split(",")[1]) for y in lines]

    xmax = max(x)
    ymax = max(y)

    surface = dict()
    ignored = set()
    ignored.add(None)
    safe = 0
    for i in range(ymax + 1):
        for j in range(xmax + 1):
            loc = getClosest((j, i), x, y)
            safe_loc = safeLoc((j, i), x, y)
            if i == 0 or j == 0 or i == ymax + 1 or j == xmax + 1:
                ignored.add(loc)

            if loc in surface:
                surface[loc] += 1
            else:
                surface[loc] = 1

            if safe_loc < 10000:
                safe += 1

    for i in ignored:
        del surface[i]

    key_ = (max(surface, key=surface.get))
    print(surface[key_])
    print(safe)


def getClosest(c, x, y):
    min_i = 1e6
    closest = None
    for i in range(len(x)):
        distance = abs(c[0] - x[i]) + abs(c[1] - y[i])
        if distance == 0:
            min_i = distance
            closest = i
        elif distance < min_i:
            min_i = distance
            closest = i
        elif distance == min_i:
            closest = None

    return closest


def safeLoc(c, x, y):
    distance = 0
    for i in range(len(x)):
        distance += abs(c[0] - x[i]) + abs(c[1] - y[i])
    return distance


if __name__ == "__main__":
    input_f = "input_1.txt"
    main(input_f)
