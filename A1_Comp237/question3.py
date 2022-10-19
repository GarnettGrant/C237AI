"""
Standardize the 'weight' column to 1.
You will need to write a function to:

Divide (the remaining columns which contain nutritional information)
by (the corresponding value in the weight column)

 and you will need to

divide ((the value in the weight column) by (itself))

    in order to get 1

Example: If an observation has a weight value of 1.33 and a calorie value of 250
         if you divide 250/1.33
         you should get
            a calories value of 188
            and a weight value of 1

"""

import pandas as pd

df = pd.read_csv(
    r'G:/Centennial College 3412/Semester 3/COMP 237 - Introduction to Artificial Intelligence/A1_Mosab/cereal.csv')

working_columns = df[['Calories', 'Serving Size Weight']].to_string()  # Debugging

print(df.to_string())


def standardize():
    for i in df:
        if df[i].dtypes == "int64" or df[i].dtypes == "float64":  # columns that contain nutritional information
            print(df[i])
            for x in range(len(df)):
                print(df.loc[x, i])

                # for x in df[i]:
            #     print(x)  # values of columns that contain nutritional information depth first

    # the remaining columns which contain nutritional information
    # /
    # the corresponding value in the weight column


standardize()
