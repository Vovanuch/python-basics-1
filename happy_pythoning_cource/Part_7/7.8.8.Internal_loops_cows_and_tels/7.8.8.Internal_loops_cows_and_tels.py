'''

Старинная задача

Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля и надо купить 100 голов скота?

Примечание. Используйте вложенный цикл for.
'''
s = 100
kol = 100

price_byk = 10
price_cow = 5
price_tel = 0.5

# 10 * byk + 5 * cow + 0.5 * tel == 100
# byk max = 100 / 10 = 10
# cow max = 100 / 5 = 20
# tel max = 100 / 0.5 = 200
list_of_decisions = []
for byk in range(11):
    for cow in range(21):
        for tel in range(201):
            if (10 * byk + 5 * cow + 0.5 * tel == 100):
                list_of_decisions.append([byk, cow, tel])
                if (byk + cow + tel == 100):
                    print(f'Solution: byks = {byk}, cows = {cow}, tels = {tel}')