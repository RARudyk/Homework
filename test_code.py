class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def dict_from_class(self):
        _excluded_keys = set(AddressBook.__dict__.self())
        return dict(AddressBook(self)
                    for (key, value) in self.__dict__.AddressBook(self)
                    if key not in _excludet_keys)



a1 = AddressBook('23','Rom', '0962076022', 'Lviv', 'r.a.rudyk@gmail.com','23-09-1984','XX')


print(a1.name)
print(a1.key)
a1.key = 34
print(a1.key)


#context maneger 20/07/2021

a = 3
b = 2
try:
    try:
        c = a / b
    except ZeroDivisionError:
        c = 0
    except (TypeError, ValueError) as ex:
        print("What a Fuck")
        raise ex
    except TypeError:
        print("a or b is not number (int)")
    # except Exception:
    #     print()
    else:
        print("else")
    finally:
        print("finally")
except TypeError:
    print("Type error except")


print(c)


# try:
#     raise Exception(1, "33", 8)
#     a = int("qwe")
# except ValueError as ex:
#     print(ex.args)

# class MyException:
#     pass
#
#
# def func():
#     f = 0
#     a = 0
#     while True:
#         f += 1
#         a += 1
#         if f == 10:
#             raise MyException()
#         if a == 5:
#             raise MyException()
#
#
# try:
#     func()
# except MyException:
#     print("func finish")
# except MyException1:
#     print("func finish")

# Logging


import logging

template = "%(levelname)s : %(name)s : %()s - %(massege)s"
# для вказування з котрого рівня показувати помилку
logging.basicConfig(level=logging.DEBUG)
# для запису логів у файл
# logging.basicConfig(level=logging.DEBUG, filename="logging.log", filemode=template)
# logging.basicConfig(level=logging.DEBUG, filename="logging.log", filemode="a")

logging.debug("debug msg")
logging.info("info msg")
logging.warning("warning msg")
logging.error("error msg")
logging.critical("critical msg")



# next
from logging import handlers

logging.basicConfig(level=logging.DEBUG)

logger = logging.getlogger(__name__)
logger.setlevel(logging.DEBUG)

s_handler = logging.StreamHandler()
s_handler.setLevel(logging.ERROR)
logger.addHandler(s_handler)
s_format = logging.Formatter('%(name)s - %(levelname)s - %(massege)s')
s_handler.setFormatter(s_format)
logger.addHandler(s_handler)

f_handler = logging.FileHandler(filename="log.log")
f_handler.setLevel(logging.DEBUG)
logger.addHandler(f_handler)

logger.debug("debug msg")
logger.info("info msg")
logger.warning("warning msg")
logger.error("error msg")
logger.critical("critical msg")
