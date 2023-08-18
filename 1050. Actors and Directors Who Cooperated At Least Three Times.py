import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director
    df_actor = df.groupby(['actor_id','director_id']).agg({'timestamp' : 'count'}).reset_index()
    df_count = df_actor[df_actor['timestamp'] >= 3]
    return df_count[['actor_id','director_id']]