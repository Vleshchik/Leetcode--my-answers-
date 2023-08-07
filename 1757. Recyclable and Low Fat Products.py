# Write your MySQL query statement below
# select product_id from products where low_fats = 'Y' and recyclable = 'Y'


import pandas as pd
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    return products[mask][['product_id']]
