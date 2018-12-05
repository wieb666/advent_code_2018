import string


def main(input_file):
    lines = open(input_file).read().strip()
    letters = list(string.ascii_lowercase)
    dict_m = {}
    for c in letters:
        dict_m[c.lower()] = c.upper()
        dict_m[c.upper()] = c.lower()

    res = polymer(lines, dict_m)
    print("Length of non reacting polymer: " + str(len(res)))

    shortest = None
    for c in letters:
        new_str = lines.replace(c, "").replace(c.upper(), "")
        res = polymer(new_str, dict_m)

        new_str_len = len(res)
        if not shortest:
            shortest = new_str_len
        if new_str_len < shortest:
            shortest = new_str_len
    print("Shortest polymer is: " + str(shortest))


def polymer(lines, dict_m):
    res = []
    for c in lines:
        if res and c == dict_m[res[-1]]:
            res.pop()
        else:
            res.append(c)
    return res


if __name__ == '__main__':
    input_f = 'input_1.txt'
    main(input_f)
