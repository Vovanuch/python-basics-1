#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_gold(arr, s, arr_res):
    for i in arr:
        if s in i:
            arr_res.append(i)



things = ['gold_pen', 'silver_leg', 'gold_hand', 'bronze_arm', 'steel_finger', 'gold_nose']
print('All things are:', *things)

golds = []
#golds = list(filter())

check_gold(things, 'gold', golds)
print('Gold things are:', *golds)
