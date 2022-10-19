"""
Question 2. (2 points)
• Identify the negative values in the data set
and replace them with the median value for that column.

"""
import pandas as pd
import statistics as st

df = pd.read_csv(
    r'G:/Centennial College 3412/Semester 3/COMP 237 - Introduction to Artificial Intelligence/A1_Mosab/cereal.csv')


# print(df.to_string())

def find_and_replace():
    for i in df:
        print(i)
        if df[i].dtypes == "int64" or df[i].dtypes == "float64":
            numbers = []
            median = 0.0
            # Calculate and display median #####################
            for x in df[i]:
                numbers.append(x)

            median = st.median(numbers)
            print("Median for {}: {}".format(i, median))  # Debugging
            ####################################################
            # Find and replace negative values #################
            for x in df[i]:
                if int(x) < 0:
                    print("x before switch: {}".format(x))  # Debugging
                    df.replace(x, str(median), inplace=True)
                    # x = str(median)   # Debugging
                    print("x after swtich: {}".format(x))  # Debugging
                else:
                    print("Not negative")  # Debugging
            ####################################################
        else:
            print("Not a number type")  # Debugging


find_and_replace()
print(df.to_string())
