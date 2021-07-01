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
#String formatting:
#Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches."
print('\ntask_4')
print(isinstance(int_a, type(int_a)), 'format from f.type is > ', type(int_a))
print(isinstance(str_b, type(str_b)), 'format from f.type is > ', type(str_b))
print(isinstance(set_c, type(set_c)), 'format from f.type is > ', type(set_c))
print(isinstance(lst_d, type(lst_d)), 'format from f.type is > ', type(lst_d))
print(isinstance(dict_e, type(dict_e)), 'format from f.type is > ', type(dict_e))

print('Anna has {0} apples and {1} peaches'.format("273", "357"))

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

#




