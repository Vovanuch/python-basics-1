#!/usr/bin/env python3
# -*- coding: utf-8 -*-

distances_in_miles = [1, 2.5, 4, 10]
print('distances in miles is:', distances_in_miles)

distances_in_km = list(map(lambda x: x*1.6, distances_in_miles))
print('distances in kilometers is:', distances_in_km)
