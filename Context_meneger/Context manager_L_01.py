# Task 1
# У файлі task1.txt знаходиться текст субтитрів взятий з відео на ютубі. Текст
# складається з міток часу і репліки яка була сказана в той момент часу.
# Причому репліка знаходиться в наступному рядку після мітки часу.
# Прочитайте вміст файлу
# Результатом виконнання завдання повинно бути:
# 1. словник елементами якого буде пара ключ:значення де ключ - мітка часу,
# значення - репліка в даний момент часу
# 2. файл в якому знаходиться текст з якого видалені всі мітки часу. всі
# субтитри повинні мати вигляд простого тексту.
# Це означає що окрім видалення міток часу, вам потрібно видалити переноси
# рядків

with open(r"task1.txt") as text:
    dict_subtitles = {}
    subtitles = text.readlines()
    for s in range(0, len(subtitles), 2):
        subtitles[s] = subtitles[s].replace("\n", "")
        subtitles[s + 1] = subtitles[s + 1].replace("\n", " ")
        dict_subtitles.update({subtitles[s]: subtitles[s + 1]})
print(dict_subtitles)

with open("task1_sub.txt", "w") as text2:
    for sub in dict_subtitles.values():
        text2.write(f"{sub}")

with open(r"task1_sub.txt") as text2:
    print(text2.read())

# Task 2
# в файлі task2 збережений список, відкрийте цей файл, прочитайте вміст, і
# знайдіть середнє арифметичне чисел що знаходяться в списку


import pickle

file = open(r"task2", "rb")
value = pickle.load(file)

print(value)
average = sum(value) / len(value)
print(average)

# Task 3
# Використовуючи openpyxl (або будь-яку іншу зручну для вас бібліотеку),
# напишіть контекстний менеджер для роботи з ексель.
# Даний менеджер повинен бути аналогом методу open()


import xlsxwriter


class CreateWorkbook:
    def __init__(self, filepath):
        self.file_obj = xlsxwriter.Workbook(filepath)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, f_type, f_value, f_traceback):
        self.file_obj.close()


with CreateWorkbook("homework.xlsx") as file:
    currency_format = file.add_format({'num_format': '$#,##0.00'})
    create_ws1 = file.add_worksheet("Start")
    create_ws2 = file.add_worksheet("Base")
    print(file.sheetnames)
    create_ws1.write(0, 0, "Hello")
    create_ws1.write(0, 1, "World!")
    create_ws1.write(0, 2, '=A1&" "&B1')
    create_ws1.write_comment(0, 0, 'This is very interesting library')

    create_ws2.write("A1", 23)
    create_ws2.write("A2", 3)
    create_ws2.write("A3", 12)
    create_ws2.write("A4", '=SUM(A1:A3)', currency_format)
    # file.close()
