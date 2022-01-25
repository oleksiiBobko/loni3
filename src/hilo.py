import random

def play():

    num = random.randint(1, 9)

    while True:
        guess = int(input("Enter the number:"))
        if num < guess:
            print("lesser")
        elif num > guess:
            print("Bigger")
        else:
            print("Bingo. Number is: ", num)
            break

if __name__ == "__main__":
    play()