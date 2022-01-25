import random
import sys

def generate_codes(size):
    codes = []

    c = 0
    while c < size:

        n = random.randint(0, 9)
        if n not in codes:
            codes.append(n)
            c += 1

    return codes

def list_has_duplicates(collection):
    unique = set(collection)

    if len(unique) == len(collection):
        return False
    else:
        return True

def count_cows(secret, digits):
    cows = 0
    i = 0
    for c in digits:
        if c in secret and secret[i] != digits[i]:
            cows += 1
        i += 1

    return cows

def count_bulls(secret, digits):
    bulls = 0
    for i in range(len(digits)):
        if secret[i] == digits[i]:
            bulls += 1

    return bulls

if __name__ == "__main__":
    print("Welcome to the Cows and Bulls game!")
    secret = generate_codes(4)

    bulls = 0
    steps = 0

    while bulls != 4:
        user_input = input("Enter a number: ")
        steps += 1

        if user_input == "exit":
            sys.exit()

        digits = [int(a) for a in str(user_input)]

        if len(digits) != 4:
            print("Invalid input")
            continue


        if list_has_duplicates(digits):
            print("Duplications are not allowed")
            continue

        cows = count_cows(secret, digits)
        bulls = count_bulls(secret, digits)

        if bulls == 4:
            print("Victory: ", secret, " it took only ", steps, " steps")

        print(cows, " cows, ", bulls, " bulls")

