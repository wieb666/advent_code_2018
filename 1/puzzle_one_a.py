from collections import Counter

input_f = "input_1.txt"

amount = 0
with open(input_f) as f:
    for line in f:
        line.strip()
        amount += int(line)

print(amount)
