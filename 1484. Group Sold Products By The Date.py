import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {'num_sold': ('product', 'nunique'), 'products': ('product', lambda x: ','.join(sorted(set(x))))}
    df = activities.groupby('sell_date').agg(**agg_dict).reset_index()
    return df