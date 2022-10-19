"""
**Question 1.**  _(4 points)_
* Create a new 'Type of Cereal' column in your dataframe (1 point) by copying the 'name' column.

Write a function to replace the names of the cereal in your new column with one of these categories
Bran, Wheat, Fiber, Protein, Crunch, Corn, Nut, Rice and Other (3 points).

Hint: the function should look through the text in the cereal name and determine, based on its contents,
how to categorize the cereal type.
"""
import pandas as pd

df = pd.read_csv(
    r'G:/Centennial College 3412/Semester 3/COMP 237 - Introduction to Artificial Intelligence/A1_Mosab/cereal.csv')

type_of_cereal = df['Cereal Name'].copy()

df['Type of Cereal'] = type_of_cereal


def replace_with_type():
    new_type_of_cereal = df['Type of Cereal'].copy()  # Created a Temporary Column to store new values

    for i in new_type_of_cereal.index:  # Looped through every index value in the Temp Column and replaced values
        if 'Bran' and 'Wheat' and 'Fiber' and 'Protein' and 'Crunch' and 'Corn' and 'Nut' and 'Rice' not in i:
            new_type_of_cereal[i] = 'Other'
        if 'Bran' in i:
            new_type_of_cereal[i] = 'Bran'
        if 'Wheat' in i:
            new_type_of_cereal[i] = 'Wheat'
        if 'Fiber' in i:
            new_type_of_cereal[i] = 'Fiber'
        if 'Protein' in i:
            new_type_of_cereal[i] = 'Protein'
        if 'Crunch' in i:
            new_type_of_cereal[i] = 'Crunch'
        if 'Corn' in i:
            new_type_of_cereal[i] = 'Corn'
        if 'Nut' in i:
            new_type_of_cereal[i] = 'Nut'
        if 'Rice' in i:
            new_type_of_cereal[i] = 'Rice'

    df['Type of Cereal'] = new_type_of_cereal.values  # Replaced column in original DataFrame with Updated data
if __name__ == "__A1_Mosab__":
    replace_with_type()  # Run Function
    print(df.to_string())  # Display DataFrame
