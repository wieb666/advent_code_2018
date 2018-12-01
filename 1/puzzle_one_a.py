def main(input_f):
    amount = 0
    with open(input_f) as f:
        for line in f:
            line.strip()
            amount += int(line)

    print(amount)


if __name__ == '__main__':
    main("input_1.txt")
