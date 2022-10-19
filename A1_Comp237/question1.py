import pandas as pd

df = pd.read_csv(
    r'G:/Centennial College 3412/Semester 3/COMP 237 - Introduction to Artificial Intelligence/A1_Mosab/cereal.csv')

type_of_cereal = df['Cereal Name'].copy()

df['Type of Cereal'] = type_of_cereal


def replace_with_type():
    new_type_of_cereal = df['Type of Cereal'].copy()

    for i in new_type_of_cereal.index:
        if 'Bran' in new_type_of_cereal[i]:
            new_type_of_cereal[i] = 'Bran'
        elif 'Wheat' in new_type_of_cereal[i]:
            new_type_of_cereal[i] = 'Wheat'
        elif 'Fiber' in new_type_of_cereal[i]:
            new_type_of_cereal[i] = 'Fiber'
        elif 'Protein' in new_type_of_cereal[i]:
            new_type_of_cereal[i] = 'Protein'
        elif 'Crunch' in new_type_of_cereal[i]:
            new_type_of_cereal[i] = 'Crunch'
        elif 'Corn' in new_type_of_cereal[i]:
            new_type_of_cereal[i] = 'Corn'
        elif 'Nut' in new_type_of_cereal[i]:
            new_type_of_cereal[i] = 'Nut'
        elif 'Rice' in new_type_of_cereal[i]:
            new_type_of_cereal[i] = 'Rice'
        else:
            new_type_of_cereal[i] = 'Other'

    df['Type of Cereal'] = new_type_of_cereal


replace_with_type()
print(df.to_string())
