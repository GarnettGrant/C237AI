# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:51:51 2022

@author: net_g
"""

import statistics

mark1 = 79
mark2 = 82
mark3 = 45

user_marks_ary = [mark1,mark2,mark3]
user_marks_tpl = (mark1,mark2,mark3)
#Calculate the AVG
#Show if the user passed or fail

average = round(statistics.mean(user_marks_tpl),2)

if (average < 50):
    print("You've failed, your average is:", average,"%")
else:
    print("You've passed!, your average is:", average,"%")