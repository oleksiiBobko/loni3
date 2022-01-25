

def do():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 13, 13, 13]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    if len(a) > len(b):
        longest_list = a
        lesser_list = b
    else:
        longest_list = b
        lesser_list = a

    result = []

    for i in longest_list:
        if (i in lesser_list and i not in result):
            result.append(i)
    print(result)

if __name__ == "__main__":
    do()
