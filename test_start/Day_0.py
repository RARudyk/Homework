'''list(Список)'''
list_products = 'apple, tomato, darck_bread, long_loaf, beef, pork,\
        mushrooms, potato, pasta'
print(list_products)

list_products_1 = ['apples', 'tomato', 'duck', 'long_loaf', 'pork',\
                   'mushrooms', 'beef', 'potato', 'pasta']
print(list_products_1)
print(list_products_1[5])
print(list_products_1[4:6])
print(list_products_1)
list_products_1[2] = 'chicken'
print(list_products_1)

costs = [23, 45, 567]
number_item = [1, 2, 3]
amount = [33, 45, 5]
names = ['apples', 'pear', 'beef']

check_list = [number_item, names, amount, costs ]

print(check_list)

list_products_1.append('deer')
list_products_1.append('elephant')
list_products_1.append('caterpillar')
print(list_products_1)

del list_products_1[9:11]
print(list_products_1)

del list_products_1[4]
print(list_products_1)

concat = names + amount
print(concat)
print(names * 3)

'''cortege(кортеж) - по суті це теж що й список але без можливості змінювати його
 після створення та ще різниця у лапках список []  кортеж ()  '''

fibonacci = (0, 1, 1, 2, 3, 5, 8, 13)
print(fibonacci)
print(fibonacci[6])
'''fibonacci.append(5) 
AttributeError: 'tuple' object has no attribute 'append
'''
'''
del fibonacci[4]
TypeError: 'tuple' object doesn't support item deletion
'''

'''
Dictionary  Dict = { 'Key' : 'Text'} 
'''

cost_products = {'apple': '35.30',
                 'pear': '53.70',
                 'grape': '73',
                 'tomato': '49'}

print(cost_products)
print(cost_products['pear'])

cost_products['pear'] = '555'
print(cost_products)
del cost_products['pear']
print(cost_products)

favorite_hobby = 'fishing, hunting, traveling'
favorite_food = ' beef, apples, pizza'
task1 = favorite_hobby + favorite_food
print(task1)

roof = 3
ninja = 25
tunnel = 2
samurai = 40
print(ninja * roof, 'ninja')
print(samurai * tunnel, 'samurai')

first_name = 'Roman'
surname = 'Rudyk'
text22 = 'Hello, mr. %s %s'
print(text22 % (first_name, surname))



