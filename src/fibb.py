

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    seq_num = int(input("Enter fibb seq num: "))

    for i in range(0, seq_num):
        print(str(i) + " = " + str(fib(i)))