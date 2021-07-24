# Task 1
# Напишіть калькулятор в якого будуть реалізовані операції додавання, віднімання, множення, ділення, піднесення в степінь,
# взяття з під кореня, пошук відсотку від числа
# калькулятор працює в нескінченному циклі. На кожній ітерації запитує перше число, операцію, друге число, після чого робить певну операцію з цими числами
#
# Огорніть в конструкцію try... except... потенційно "небезпечні" місця, наприклад отримання числа і приведення до типу даних
# або інструкції математичних операцій (ділення на нуль, наприклад)
#
# заповніть ваш скрипт логами
# Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
# + логи з помилками
# причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
# лог файл завжди відкривається в режимі дозапису.
# так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки

import logging

try:
    file = open("hw10_log.log", 'r')
except:
    file = open("hw10_log.log", 'w')
finally:
    file.close()

log_template = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, filename="hw10_log.log", filemode="a", format=log_template)


def add():
    logging.info("calling add_func")
    str_a = input('first num: ')
    try:
        a = int(str_a)
    except ValueError:
        print('a is not decimal')
        logging.error('not decimal first number to add')
        return
    str_b = input('second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to add')
        return
    c = a + b
    print(f"{a} + {b} = {c}")
    logging.info(f"add is successfully finished, {a}, {b}")
    return c


def subtraction():
    logging.info("calling subtraction")
    str_a = input('first num: ')
    try:
        a = int(str_a)
    except ValueError:
        print('a is not decimal')
        logging.error('not decimal first number to subtraction')
        return
    str_b = input('second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to subtraction')
        return
    c = a - b
    print(f"{a} - {b} = {c}")
    logging.info(f"subtraction is successfully finished, {a}, {b}")
    return c


def multiplication():
    logging.info("calling multiplication")
    str_a = input('first num: ')
    try:
        a = int(str_a)
    except ValueError:
        print('a is not decimal')
        logging.error('not decimal first number to multiplication')
        return
    str_b = input('second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to multiplication')
        return
    c = a * b
    print(f"{a} * {b} = {c}")
    logging.info(f"multiplication is successfully finished, {a}, {b}")
    return c


def division():
    logging.info("calling division")
    str_a = input('first num: ')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to division')
        return
    str_b = input('second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to division')
        return
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
        logging.info(f"division is successfully finished, {a}, {b}")
        return c
    except ZeroDivisionError:
        print("b is 0, ZeroDivisionError")
        logging.error('trying to divide by zero')
        return


def exaltation():
    logging.info("calling exaltation")
    str_a = input('first num: ')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to exaltation')
        return
    str_b = input('second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to exaltation')
        return
    try:
        c = a ** b
    except ZeroDivisionError:
        print("0 ^ -1 can't be compute")
        logging.error('trying 0 ^ -1')
        return
    print(f"{a} ^ {b} = {c}")
    logging.info(f"exaltation is successfully finished, {a}, {b}")
    return c


def root():
    logging.info("calling root")
    str_a = input('first num: ')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to root')
        return
    str_b = input('second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to root')
        return
    try:
        c = a ** (1 / b)
        print(f"{a} ^ {b} = {c}")
        logging.info(f"root is successfully finished, {a}, {b}")
        return c
    except ZeroDivisionError:
        print("b is 0, can't get root, ZeroDivisionError")
        logging.error('trying to divide by zero (in degree)')
        return


def percentage():
    logging.info("calling percentage")
    str_a = input('first num: ')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to percentage')
        return
    str_b = input('second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to percentage')
        return
    c = a * b / 100
    print(f"{b}% from {a} = {c}")
    logging.info(f"percentage is successfully finished, {a}, {b}")
    return c


# add()
# subtraction()
# multiplication()
# division()
# exaltation()
# root()
# percentage()

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        if choice == '1':
            print(add())
        elif choice == '2':
            print(subtraction())
        elif choice == '3':
            print(multiplication())
        elif choice == '4':
            print(division())
        elif choice == '5':
            print(exaltation())
        elif choice == '6':
            print(root())
        elif choice == '7':
            print(percentage())
        break
    else:
        print("What you doings BRO")
        logging.error('BRO is very exrtaordinary')

