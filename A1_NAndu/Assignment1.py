# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:27:38 2022

@author: Nandagopan Dilip
"""

import pandas as pd
import numpy as np

#function for identifying the type of cereal present by analysing the name
def type_of_cereal(string):
    if 'bran' in string:
        return 'Bran'
    elif 'wheat' in string:
        return 'Wheat'
    elif 'fiber' in string:
        return 'Fiber'
    elif 'protien' in string:
        return 'Protien'
    elif 'crunch' in string:
        return 'Crunch'
    elif 'corn' in string:
        return 'Corn'
    elif 'nut' in string:
        return 'Nut'
    elif 'rice' in string:
        return 'Rice'
    else:
        return 'Other'
    
#find the average of a column    
def column_average(column):
    sum = 0
    for value in column:
        sum += value
    return round(sum/(len(column)), 1)

#read and print cereal.csv
df = pd.read_csv(r'./cereal.csv')
print(df)

'''question 1'''
#copy values of "Cereal Name" to another column "Type of Cereal"
df['Type of Cereal'] = df['Cereal Name']

#iterate and replace the 'Type of Cereal' based on the contents in name
for cerealType in df['Type of Cereal']:
        df['Type of Cereal'] = df['Type of Cereal'].replace([cerealType], type_of_cereal(cerealType.lower()))


'''question 2'''
#identifying each column type and getiing the negative values to replace them
for column in df:
    if df[column].dtype == np.int64 or df[column].dtype == np.float64:
        average = column_average(df[column])
        for i, value in enumerate(df[column]):
            if value < 0:
                df[column].values[i] = average


'''question 3'''
#standardizing all the rows with weight being 1 unit
for i, value in enumerate(df['Serving Size Weight']):
    if df['Serving Size Weight'].values[i] != 1:
        for column in df:
            if df[column].dtype == np.int64 or df[column].dtype == np.float64:
                df[column].values[i] /= df['Serving Size Weight'].values[i]
                df[column].values[i] = round(df[column].values[i], 2)

    
'''guestion 4'''
#creating a new column with default values as unhealthy
df['Healthy Or Not'] = 'unhealthy'

#checking if the cereal satisfies each condition of columns to be deemed healthy
for i, value in enumerate(df['Healthy Or Not']):
            if df['Calories'].values[i] < 100:
                if df['Sodium'].values[i] < 150:
                    if df['Sugars'].values[i] < 9:
                        if df['Dietary Fiber'].values[i] > 3:
                            if df['Protein (g)'].values[i] > 2:
                                df['Healthy Or Not'].values[i] = "healthy"


'''guestion 5'''
#dict to hold the manufacturers
manufacturers = {}

#iterate through each value in column and create a dict with only key being manufacturers.
for i, value in enumerate(df['Manufacturer']):
    if value not in manufacturers:
        manufacturers[df['Manufacturer'].values[i]] = [0, 0]
        
#iterate through all manufactures to get the number healthy products and no of unhealthy ones
for manufacturer in manufacturers:
    for i, value in enumerate(df['Manufacturer']):
        if value == manufacturer:
            if df['Healthy Or Not'].values[i] == 'healthy':
                manufacturers[manufacturer][0] += 1;
            elif df['Healthy Or Not'].values[i] == 'unhealthy':
                manufacturers[manufacturer][1] += 1;
                
#displaying the number of healthy and unhealthy products of each brand with the percentage distribution
for manufacturer in manufacturers:
    #calculating percentage
    if manufacturers[manufacturer][0] != 0:
        percentage = round((manufacturers[manufacturer][0]/(manufacturers[manufacturer][0] + manufacturers[manufacturer][1])) * 100, 1)
    else:
        percentage = 0.0
    #printing the values
    print(manufacturer)
    print('Healthy Products: ' + str(manufacturers[manufacturer][0]))
    print('Unhealthy Products: ' + str(manufacturers[manufacturer][1]))
    print(str(percentage) +'% percentage of cereals produced by ' + manufacturer + ' is healthy\n')


'''guestion 6'''
print('\nRatings\n')
#displaying the number of healthy and unhealthy products of each brand with the percentage distribution
for manufacturer in manufacturers:
    #calculating percentage
    if manufacturers[manufacturer][0] != 0:
        percentage = round((manufacturers[manufacturer][0]/(manufacturers[manufacturer][0] + manufacturers[manufacturer][1])) * 100, 1)
    else:
        percentage = 0.0
    #printing the values
    print(manufacturer)
    print('Healthy Products: ' + str(manufacturers[manufacturer][0]))
    print('Unhealthy Products: ' + str(manufacturers[manufacturer][1]))
    print(str(percentage) +'% percentage of cereals produced by ' + manufacturer + ' is healthy\n')
print(df)