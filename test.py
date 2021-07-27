
def exaltation():
    str_a = input('first num: ')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        return
    str_b = input('second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        return
    try:
        c = a ** b
    except ZeroDivisionError:
        print("0 ^ -1 can't be compute")
        return
    print(f"{a} ^ {b} = {c}")
    return c

exaltation()
