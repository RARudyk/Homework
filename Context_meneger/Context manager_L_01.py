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
