def main(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    f = 0
    seen = set()
    while True:
        for x in data:
            f += int(x)
            if f in seen:
                print(f)
                exit()
            seen.add(f)


if __name__ == '__main__':
    input_f = "input_2.txt"
    main(input_f)
