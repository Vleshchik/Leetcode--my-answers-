import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    valid_patients_df = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    return valid_patients_df[['patient_id', 'patient_name', 'conditions']]