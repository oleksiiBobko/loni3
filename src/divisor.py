

def do():
    number = int(input("Enter a number"))

    list_range = list(range(1, number + 1))

    divisor_list = []


    for i in list_range:
        if number % i == 0:
            divisor_list.append(i)

    print(divisor_list)

if __name__ == "__main__":
    do()
