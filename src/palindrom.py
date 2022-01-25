

def reverce():
    inp = str(input("Enter something:")).lower()

    output = ""

    for c in inp:
        if c.isalnum():
            output = output + c

    if output == output[::-1]:
        print("is palindrome")
    else:
        print("is not palindrome")


if __name__ == "__main__":
    reverce()
