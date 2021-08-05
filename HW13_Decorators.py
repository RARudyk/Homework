# 1. Написати функцію яка в циклі зчитує з консолі
# введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції
import time


def work_time(write):
    def wrap(*args, **kwargs):
        t1 = time.time()
        result = write(*args, **kwargs)
        print(time.time() - t1)
        return result

    return wrap


@work_time
def write_word():
    new_list = []
    text = input("Please write your text, number or cancel with Exit == E: ")
    while text:
        new_list.append(text)
        if input() == 'E':
            break
    return new_list


work_time(write_word())

# 2. Написати функцію яка приймає два катети і повертає
# значення гіпотензузи. Написати декоратор на функцію,
# який виводить на екран текст з довжиною катетів і гіпотенузи.
# Важливо! Функція повинно повернути саме значення гіпотенузи як число,
# а декоратор повинен зробити вивід на екран
# наприклад такого тексту “При катетах 3, 4 – гіпотенуза дорівнює 5”.

def view_hypo(hypo_):
    def wrap(x, y):
        print(f'In legs {x} , {y} the hypotenuse is equal to : {hypo_(x, y)}')
    return wrap


@view_hypo
def hypo(x, y):
    hypotenuse = (x ** 2 + y ** 2) ** 0.5
    return hypotenuse


hy = view_hypo(hypo(1, 4))


# 3. Написати функцію яка приймає список елементів і знаходить суму,
# до функції написати декоратор який перед тим як
# запустити функцію видаляє з списку всі не чисельні типи даних,
# але якщо є строка яку можна перевести в число,
# (наприклад “1”) то строка приводиться до чисельного типу даних

def filter_list(add_):
    def wrap(x):
        res = []
        for ele in x:
            try:
                res.append(float(ele))
            except ValueError:
                continue
        return add_(res)
    return wrap


@filter_list
def add_list(lis):
    return sum(lis)


list_ad = ['gfg', '45.45', 'is', '87.5', 'best', '90.34']

print(add_list(list_ad))


# 4. Написати функцію яка приймає на вхід ціле число n створює і
# повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого
# списку переведе в строковий тип даних
def decor_for_int(integer_):
    def wrap():
        return [str(n) for n in integer_()]
    return wrap


@decor_for_int
def integer():
    new_list = []
    inp = int(input('Please input your number: '))
    for n in range(inp):
        new_list.append(n)
    # result = [new_list.append(n) for n in range(inp)]
    return new_list


print(integer())
