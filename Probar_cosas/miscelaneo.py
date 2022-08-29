from multiprocessing.sharedctypes import Value


def func():
    a = input("Dame un número")
    try:
        return int(a)

    except ValueError:
        return func()

func()