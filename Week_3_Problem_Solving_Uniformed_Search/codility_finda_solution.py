# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:10:17 2022

@author: net_g

Informed Strategy
"""
A = [1,2,3,4,5,6,7,8]



def solution_a(A):
    min_val = 100000
    set_a = set(A)
    for num in range(1, 100000):
        if 0 < num < min_val and num not in set_a:
            min_val = num
    return min_val

print(solution_a(A))