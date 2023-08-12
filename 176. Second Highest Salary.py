# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
<<<<<<< HEAD
WHERE salary < (SELECT MAX(salary) FROM Employee);

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary_df = employee['salary'].sort_values(ascending=False).drop_duplicates()
    return pd.DataFrame({'SecondHighestSalary':[salary_df.iloc[1]]}) if len(salary_df) > 1 else pd.DataFrame({'SecondHighestSalary':[None]})
=======
WHERE salary < (SELECT MAX(salary) FROM Employee);
>>>>>>> origin/main
