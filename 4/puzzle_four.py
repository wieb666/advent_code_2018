from collections import defaultdict


def main(sorted_lines):
    C = defaultdict(int)
    CM = defaultdict(lambda: defaultdict(int))
    CMM = defaultdict(int)
    guard = None
    asleep = None
    for line in sorted_lines:
        if line:
            time = parseTime(line)
            if 'begins shift' in line:
                guard = int(line.split()[3][1:])
                asleep = None
            elif 'falls asleep' in line:
                asleep = time
            elif 'wakes up' in line:
                for t in range(asleep, time):
                    CM[guard][t] += 1
                    CMM[(guard, t)] += 1
                    C[guard] += 1

    best_guard = argmax(C)
    best_min = argmax(CM[best_guard])
    print(best_guard, best_min)
    print(best_guard * best_min)

    best_guard, best_min = argmax(CMM)
    print(best_guard, best_min)
    print(best_guard * best_min)


def parseTime(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])


def argmax(d):
    best = None
    for k, v in d.items():
        if best is None or v > d[best]:
            best = k
    return best


if __name__ == "__main__":
    lines = open("input_1.txt").read().split("\n")
    lines.sort()
    main(lines)
