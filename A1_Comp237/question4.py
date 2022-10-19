"""
Question 4: Create a new column to categorize cereals as 'healthy' vs 'unhealthy'.

Healthy Cereals:
                Low Calories(<100),
                Low Sodium(<150),
                Low Sugar(<9),
                High fiber(>3),
                High Protein(>2),

Unhealthy:      (Other)

Name: Garnett Grant
Student Number: 301188923
Date: Oct 5th 2022
File name: question4.py
"""

import pandas as pd

df = pd.read_csv(
    r'G:/Centennial College 3412/Semester 3/COMP 237 - Introduction to Artificial Intelligence/A1_Mosab/cereal.csv')


def create_column():
    df['Healthy vs Unhealthy'] = 'Unhealthy'


def categorize_cereals():
    create_column()
    for i in df.index:
        if int(df['Calories'][i]) < 100:
            if int(df['Sodium'][i]) < 150:
                if int(df['Sugars'][i]) < 9:
                    if int(df['Dietary Fiber'][i]) > 3:
                        if int(df['Protein (g)'][i]) > 2:
                            df['Healthy vs Unhealthy'][i] = "Healthy"
    print(df.to_string())


categorize_cereals()
# print(df.to_string())
