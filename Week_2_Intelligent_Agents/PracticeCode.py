# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:04:31 2022

@author: net_g
"""
#Calculate the AVG
#Show if the user passed or fail

from bigO import BigO
from bigO import algorithm

def calculate_marks:
    
    marks = [79,82,45]
    sum = 0

    for i in marks:
    sum += i
    
    sum /= 3

    if (sum < 50):
        print(f"You've failed, your average is: {round(sum,2)}%")
    else:
        print(f"You've passed!, your average is: {round(sum,2)}%")


