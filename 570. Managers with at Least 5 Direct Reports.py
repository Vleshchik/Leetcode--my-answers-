# Write your MySQL query statement below

'''SELECT E1.name FROM Employee E1
JOIN  (SELECT managerId FROM Employee GROUP BY managerId HAVING COUNT(managerId) >= 5)  E2 ON E1.id = E2.managerId'''


import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    output = employee.groupby(['managerId'])['id'].agg(['count']).reset_index()
    output = output.loc[output['count']>=5,['managerId']]
    output = employee.loc[employee['id'].isin(output['managerId']),['name']]

    return output