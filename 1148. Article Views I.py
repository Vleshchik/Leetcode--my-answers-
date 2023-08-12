# Write your MySQL query statement below
select distinct author_id as id from views where author_id = viewer_id order by id ASC

import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views['author_id'] == views['viewer_id']][['author_id']].drop_duplicates().rename(columns={'author_id': 'id'}).sort_values(by='id', ascending=True)