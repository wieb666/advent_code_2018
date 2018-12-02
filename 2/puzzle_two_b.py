def main(input_f):
    input_lines = []
    with open(input_f) as f:
        for line in f:
            line = line.strip()
            input_lines.append(line)

    for l in input_lines:
        for l2 in input_lines:
            if l2 == l:
                continue
            wrong = 0
            left = ""
            for c_i in range(len(l)):
                if wrong > 1:
                    break
                if l[c_i] != l2[c_i]:
                    wrong += 1
                    continue
                left = left + l[c_i]
            if len(left) == len(l) - 1:
                print(left)


if __name__ == '__main__':
    main("input_1.txt")
