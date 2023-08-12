# Write your MySQL query statement below
# SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000;

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_contries_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]

    return big_contries_df[['name', 'area', 'population']]