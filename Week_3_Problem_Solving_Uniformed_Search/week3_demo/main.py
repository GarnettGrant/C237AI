# -*- coding: utf-8 -*-
"""
Garnett Grant
301188923

Week 12 Excercise 2
using Pandas library , produce the following output . using pandas
data frame organize the data into rows and columns

"""

import pandas as pd

data = {
    'subject_id': [1, 2, 3, 4],
    'student_name': ['Joseph', 'Eva', 'Kevin', 'Joseph'],
    'courses': ['software engineering', 'Artificial Intelligence', 'Gaming', 'Software engineering technician']
}

students_and_courses_list = pd.DataFrame(data)  # DataFrame: 2d Data Structure (2d Array/Table with rows and columns)

print(students_and_courses_list)

print('\n')  # Space Divider

print(students_and_courses_list.loc[0])  # Locate Row (Changes format aka Series)

print('\n')  # Space Divider

print(students_and_courses_list.loc[[0]])  # Locate Row (Keeps format aka DataFrame)
