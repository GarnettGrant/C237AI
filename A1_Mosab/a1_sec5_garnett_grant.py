import pandas as pd

df = pd.read_csv(
    r'G:/Centennial College 3412/Semester 3/COMP 237 - Introduction to Artificial Intelligence/A1_Mosab/cereal.csv')

type_of_cereal = df['Cereal Name'].copy()

df['Type of Cereal'] = type_of_cereal


def replace_with_type():
    new_type_of_cereal = df['Type of Cereal'].copy()

    for i in new_type_of_cereal.index:
        if 'Bran' and 'Wheat' and 'Fiber' and 'Protein' and 'Crunch' and 'Corn' and 'Nut' and 'Rice' not in cereal:
            new_type_of_cereal[i] = 'Other'
        if 'Bran' in cereal:
            new_type_of_cereal[i] = 'Bran'
        if 'Wheat' in cereal:
            new_type_of_cereal[i] = 'Wheat'
        if 'Fiber' in cereal:
            new_type_of_cereal[i] = 'Fiber'
        if 'Protein' in cereal:
            new_type_of_cereal[i] = 'Protein'
        if 'Crunch' in cereal:
            new_type_of_cereal[i] = 'Crunch'
        if 'Corn' in cereal:
            new_type_of_cereal[i] = 'Corn'
        if 'Nut' in cereal:
            new_type_of_cereal[i] = 'Nut'
        if 'Rice' in cereal:
            new_type_of_cereal[i] = 'Rice'

    df['Type of Cereal'] = new_type_of_cereal


replace_with_type()
print(df.to_string())
