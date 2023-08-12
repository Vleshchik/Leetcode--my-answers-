import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_without_orders = customers[~customers['id'].isin(orders['customerId'])]
    customers_without_orders = customers_without_orders[['name']].rename(columns={'name': 'Customers'})

    return customers_without_orders