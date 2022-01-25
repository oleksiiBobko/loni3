import random


def to_bool(o):
    if o == "" or o.lower() != "yes":
        return False
    else:
        return True


def split(word):
    return [char for char in word]


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

def gen_strong_password(length, use_upper_case, use_lower_case, use_numbers, use_symbols):
    matrix = []
    matrix.append(split("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    matrix.append(split("abcdefghijklmnopqrstuvwxyz"))
    matrix.append(split("0123456789"))
    matrix.append(split("~!@#$%^&*()_+=/\-`\"',.?"))

    attr = []

    if use_upper_case:
        attr.append(0)
    if use_lower_case:
        attr.append(1)
    if use_numbers:
        attr.append(2)
    if use_symbols:
        attr.append(3)

    seq = generate_seq(int(length), attr)

    result = ""

    for i in seq:
        result += random.sample(matrix[i], 1)[0]

    return result


if __name__ == "__main__":
    length = input("Enter password length: ")
    print("answer with Yes/No")
    use_upper_case = to_bool(input("Use upper case: "))
    use_lower_case = to_bool(input("Use lower case: "))
    use_numbers = to_bool(input("Include numbers: "))
    use_symbols = to_bool(input("Include symbols: "))
    print(gen_strong_password(length, use_upper_case, use_lower_case, use_numbers, use_symbols))
