# Write your MySQL query statement below
'''SELECT class FROM Courses GROUP BY class HAVING COUNT(student) >= 5;'''

import pandas as pd
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses.groupby('class')['student'].count().reset_index()
    result = class_counts[class_counts['student'] >= 5][["class"]]
    return result