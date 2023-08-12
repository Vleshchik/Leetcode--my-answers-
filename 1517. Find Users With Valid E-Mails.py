import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_emails_df = users[users['mail'].str.match(r'^[a-zA-Z][\w.-]*@leetcode\.com$', na=False)]
    return valid_emails_df[['user_id', 'name', 'mail']]