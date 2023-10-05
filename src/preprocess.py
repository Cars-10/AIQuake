import pandas as pd

def drop_columns(df):
    df.drop('column_name', axis=1, inplace=True)

    return df

