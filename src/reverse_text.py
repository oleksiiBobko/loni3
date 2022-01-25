

def reverse(a):
    return list(set(a))


if __name__ == "__main__":
    t = input("Enter text: ").split(" ")
    print(" ".join(t[::-1]))
