#1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print('\ntask_1')
print(id(int_a),id(str_b),id(set_c),id(lst_d),id(dict_e))

#2. Append 4 and 5 to the lst_d and define the id one more time.
print('\ntask_2')
b22 = [4, 5]
lst_d1 = lst_d.append(b22)
print(id(lst_d1))

#3. Define the type of each object from step 1.
print('\ntask_3')
print(type(int_a),type(str_b),type(set_c),type(lst_d),type(dict_e))

#4*. Check the type of the objects by using isinstance.

print('\ntask_4')
print(isinstance(int_a, type(int_a)), 'format from f.type is > ', type(int_a))
print(isinstance(str_b, type(str_b)), 'format from f.type is > ', type(str_b))
print(isinstance(set_c, type(set_c)), 'format from f.type is > ', type(set_c))
print(isinstance(lst_d, type(lst_d)), 'format from f.type is > ', type(lst_d))
print(isinstance(dict_e, type(dict_e)), 'format from f.type is > ', type(dict_e))

#String formatting:
#Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches."
#print('Anna has {0} apples and {1} peaches'.format("273", "357"))

#5. With .format and curly braces {}
print('\ntask_5')
print('Anna has {} apples and {} peaches'.format(3, 33))

#6. By passing index numbers into the curly braces.
print('\ntask_6')
print('Anna has {0} apples and {1} peaches'.format(23, 2))

#7. By using keyword arguments into the curly braces.
print('\ntask_7')
print('Anna has {0} apples and {rr} peaches'.format(12, rr="43"))

#8*. With indicators of field size (5 chars for the first and 3 for the second)
print('\ntask_8')
print('Anna has {0:5} apples and {1:3} peaches'.format(12, "43"))

#9. With f-strings and variables
print('\ntask_9')
apples = 5
peaches = 13
print(F'Anna has {apples} apples and {peaches} peaches')

#10. With % operator
print('\ntask_10')
app = "three"
pea = "fifteen"
print('Anna has %s apples and %s peaches'% (app, pea))

#11*. With variable substitutions by name (hint: by using dict)
print('\ntask_11')
app1 = "eighteen"
pea1 = "twelve"
data_dict = {"RE": app1, "me": pea1}
print('Anna has %(RE)s apples and %(me)s peaches'% data_dict)

#Comprehensions:
#(1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
print(type(lst))

#12. Convert (1) to list comprehension
print('\ntask_12')
list_compr = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)  ]
print(list_compr)

#13. Convert (2) to regular for with if-else
print('\ntask_13')
#(2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

tes = []
for num in range(10):
    if num % 2 == 0:
        tes.append(num // 2)
    else:
        tes.append(num * 10)
print(tes)



print('next task-- >14')
#(3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
#14. Convert (3) to dict comprehension.
print('\ntask_14')
dict_comp = {num: num ** 2 for num in range(1, 11) if num % 2 == 1 }
print(dict_comp)

print('next task-- >15')
#(4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
#15*. Convert (4) to dict comprehension.
print('\ntask_15')
dic_com_4 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dic_com_4)


print('next task-- >16')
#(5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)
#16. Convert (5) to regular for with if.
print('\ntask_16')
dict_5 = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_5[x] = x**3
print(dict_5)

print('next task-- >17')
#(6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
#17*. Convert (6) to regular for with if-else.
print('\ntask_17')
lis_6 = {}
for x in range(10):
    if x**3 % 4 == 0:
        lis_6[x] = x**3
    else:
        lis_6[x] = x
print(lis_6)

print('next task-- >18')
#Lambda:
#(7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y

#18. Convert (7) to lambda function
print('\ntask_18')
foo_7 = lambda x, y : x if(x < y) else y

print('next task-- >19')
#(8)
foo = lambda x, y, z: z if y < x and x > z else y

#19*. Convert (8) to regular function
print('\ntask_19')
def foo_8(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

print('next task-- >20,..,22')

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

#20. Sort lst_to_sort from min to max
#21. Sort lst_to_sort from max to min
#22. Use map and lambda to update the lst_to_sort by multiply each element by 2

#23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]