found_coind = 20
magic_coins = 10
lost_coins = 3
year = 365
amount_weeks = 52

all = found_coind + magic_coins * year - lost_coins * amount_weeks

print(found_coind)
print(all)

magic_coins = 13
lost_coins = 2
all1 = found_coind + magic_coins * year - lost_coins * amount_weeks
print(all1)
message_0 = 'Friend, you have a nice suit'
message = '''Is it very cold today?     
Yes or no'''
print(message_0)
print(message)

''' (\' - називається екранування для пропуску лапок (дозволяє не розривати стрічку))'''
man_say = 'Він сказав: "там в\'ється бур\'ян дерев\'яним п\'єдесталом."'
print(man_say)
man_say_1 = "Він сказав: 'там в'ється бур'ян дерев'яним п'єдесталом.'"
print(man_say_1)
man_say_2 = '''Він сказав: "там в'ється бур'ян дерев'яним п'єдесталом."'''
print(man_say_2)

degrees = 14
text = "today is %s degrees"
print(text % degrees)

temperature = 34
text_1 = "today is wednesday and enough hot air, temperature is more than %s degrees celsius "
print(text_1 % temperature)
print(text_1 % degrees)
text_2 = "my weight is less than %s, but more than %s kilograms"
print(text_2 % (temperature, degrees))

