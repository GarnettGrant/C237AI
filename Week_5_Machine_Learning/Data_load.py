# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:10:30 2020

@author: mhabayeb
"""

import pandas as pd
import os

# neat way
filename = 'Advertising.csv'
path = 'G:/Centennial College 3412/Semester 3/COMP 237 - Introduction to Artificial Intelligence/Week_5_Machine_Learning/'
fullpath = os.path.join(path, filename)
###
data_mayy_adv = pd.read_csv(fullpath)
##
data_mayy_adv.head(5)
###
data_mayy_adv.dtypes
###
data_mayy_adv.describe()
###
data_mayy_adv.shape

#########
data_mayy_medals = pd.read_csv('http://winterolympicsmedals.com/medals.csv')
data_mayy_medals.tail(2)
data_mayy_medals.dtypes
data_mayy_medals.describe()
