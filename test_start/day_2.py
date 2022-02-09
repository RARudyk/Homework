age = 13
if age > 20:
    print('old Man')
elif age == 13:
    print('Men_weirdo')
else:
    print('fine?')


'''are you rich'''
money = '10001'
f_money = float(money)
if f_money > 1000 and f_money <= 5000:
    print('You do no have enough money to be a rich!')
elif f_money > 5000 and f_money <= 10000:
    print('Men you have money!')
elif f_money > 10000:
    print('You have doing money every day, day by day.')
else:
    print('BRO, you have go to work')

'''kendy'''
kendy = 500
if kendy <= 100:
    print('not a lot')
elif kendy >= 500:
    print('Too much')
else:
    print('Ok')

'''right number'''
cash = 800
if (cash > 100 and cash < 500) or (cash > 1000 and cash < 5000) :
    print('right number')
else:
    print('not in range')

'''i can to fight these ninja and i will win them'''
ninja = 50
if ninja < 10:
    print('i can win at these ninja')
elif ninja < 30 and ninja >= 10:
    print('it wil been hard but i will have won by them')
elif ninja < 50 and ninja >=30:
    print('Too much, to win')
else:
    print('in total, ninja more than 50')

