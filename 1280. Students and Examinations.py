# Write your MySQL query statement below
'''SELECT s.student_id, s.student_name, su.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects su
LEFT JOIN Examinations e ON s.student_id = e.student_id AND su.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, su.subject_name
ORDER BY s.student_id, su.subject_name;'''

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    return students.merge(subjects, how="cross").merge(examinations[["student_id","subject_name"]].value_counts().reset_index(), how="left").fillna(0).sort_values(by=["student_id","subject_name"]).rename(columns={"count":"attended_exams"}) if not examinations.empty else pd.DataFrame(columns=["student_id","student_name","subject_name","attended_exams"])

