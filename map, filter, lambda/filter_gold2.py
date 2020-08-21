#!/usr/bin/env python3
# -*- coding: utf-8 -*-

    

things = ['gold_pen', 'silver_leg', 'gold_hand', 'bronze_arm', 'steel_finger', 'gold_nose']
print('All things are:', *things)

golds = []

# try to search gold -part in array 
finding_str = 'gold'
#check_gold(things, 'gold', golds)

golds = list(filter(lambda s: s.find(finding_str) > -1, things))
print('Gold things are:', *golds)


# тестировал лямбду как отдельную функцию по поиску вхождения
print()
fun = lambda s: s.find('gold') > -1
print(fun('golden'))
