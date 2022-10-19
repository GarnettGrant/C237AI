"""
Question 2. (2 points)
• Identify the negative values in the data set
and replace them with the median value for that column.

Name: Garnett Grant
Student Number: 301188923
Date: Oct 5th 2022
Filename: question2.py

"""
import pandas as pd
import statistics as st

df = pd.read_csv(
    r'G:/Centennial College 3412/Semester 3/COMP 237 - Introduction to Artificial Intelligence/A1_Mosab/cereal.csv')


def find_and_replace():
    for i in df:
        numbers = []
        median = 0.0
        if df[i].dtypes == "int64" or df[i].dtypes == "float64":
            # Calculate median #####################
            for x in df[i]:
                numbers.append(x)
            median = st.median(numbers)
            ####################################################

            # Find and replace negative values #################
            for x in df[i]:
                if int(x) < 0:
                    df.replace(x, str(median), inplace=True)
            ####################################################


find_and_replace()
print(df.to_string())

