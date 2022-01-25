from math import sqrt


def is_prime(num):

    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    root = int(sqrt(num))

    for i in range(3, root, 2):
        if i % 2 == 0:
            return False

    return True

if __name__ == "__main__":
    while True:
        user_input = input("Enter a number: ")

        if(user_input == "exit"):
            break

        number = int(user_input)
        
        if is_prime(number):
            print("Number is prime: ", number)
        else:
            print("Number is not prime: ", number)
