def main(input_f):
    two = 0
    three = 0
    with open(input_f) as f:
        for line in f:
            line = line.strip()
            char_dict = {}
            for char in line:
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
            if 2 in char_dict.values():
                two += 1
            if 3 in char_dict.values():
                three += 1

    print(two)
    print(three)
    total = two * three
    print(total)


if __name__ == '__main__':
    main("input_1.txt")
