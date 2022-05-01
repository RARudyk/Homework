# for - loop (відрізняється від while тим,
# що використовується коли відоме МАКС значення )

for x in range(0, 5):
    print('sweet')

for z in range(3, 7):
    print('sweet %s' % z)

print(list(range(0, 5)))

for z1 in range(0, 5):
    print('sweet %s' % (z1 + 1))


list_products_1 = ['apples', 'tomato', 'duck', 'long_loaf', 'pork',\
                   'mushrooms', 'beef', 'potato', 'pasta']

for q in list_products_1:
    print(list([q]))
for q1 in list_products_1:
    print(list(q1))
for q2 in list_products_1:
    print(q2)

list_name = ['one', 'two', 'three']
for i in list_name:
    print('1 %s' % i)
    for j in list_name:
        print('2 %s' % j)


find_coins = 20
magic_coins = (10 * 7) #10 coins for seven days per week
steal_coins = 3
coins = find_coins
for week in range(1, 53):
    coins = coins + magic_coins - steal_coins
    print('Week %s = %s coins' % (week, coins))

#t1
for x in range(0, 20):
    print('Hello %s' % x)
    if x < 9:
        break

#t2
age = 0
while age < 38:
    age = age + 2
    print(age)

# or
increase = 2    #create first variable for increase age on 2 years
age_begin = 0   #create second variable for start position for age
age_end = age_begin #create variable "end_age" as redefine variable "age_begine"
for age_1 in range(0, 38):
    age_end = age_end + increase #increase redefined variable "end_age"
    if age_end <= 38:
        print(age_end)
    else:
        break


#t3
y = 0
ingredients = ['apple', 'pain', 'peach', 'watermelon', 'strawberry', 'raspberry']
for x in ingredients:
    y = y + 1
    print('%s %s' % (y, x))

#t4
weight = 30
weight_on_moon = 0.165
weight_year = weight
for year in range(1, 16):
    weight_year = (weight_year + 1)
    weight_year_m = weight_year * weight_on_moon
    print('%s year with weight is %f' % (year, weight_year_m))

