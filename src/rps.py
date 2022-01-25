import getpass

def play():

    while True:
        print("r - rock")
        print("p - paper")
        print("s - scissors")

        first_move = input("Make first move:")
        second_move = input("Make second move:")

        if (first_move == "exit") or (second_move == "exit"):
            break

        if first_move == second_move:
            print("same moves")
            continue


        if (first_move == "p") and (second_move == "r"):
            print("first win")
            continue
        if (first_move == "r") and (second_move == "s"):
            print("first win")
            continue
        if (first_move == "s") and (second_move == "p"):
            print("first win")
            continue

        if (second_move == "p") and (first_move == "r"):
            print("second win")
            continue
        if (second_move == "r") and (first_move == "s"):
            print("second win")
            continue
        if (second_move == "s") and (first_move == "p"):
            print("second win")
            continue

        print("cycle")
        break

if __name__ == "__main__":
    play()
