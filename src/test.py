import random


def generate_seq(length, attr):
    seq = []

    while True:

        for i in range(length):
            seq.append(attr[random.randint(0, len(attr) - 1)])

        for j in attr:
            if j not in seq:
                continue

        break

    return seq

attr = [0, 1, 2, 3]

print(generate_seq(8, attr))