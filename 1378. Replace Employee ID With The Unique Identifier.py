# Write your MySQL query statement below
'''SELECT CASE
WHEN eu.unique_id IS NOT NULL
THEN eu.unique_id ELSE NULL END AS unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id;'''

import pandas as pd
def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(employees,employee_uni,how='left',on='id')
    return df[['unique_id','name']]