import datetime


def run():
    name = input("What is your name:")
    age = input("How old are you:")

    when_you_old = datetime.datetime.now() + datetime.timedelta(days = (100 - int(age)) * 365)

    print(name, " will be 100 years old at: ", when_you_old)

if __name__ == "__main__":
    run()