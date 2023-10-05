import pandas as pd

def drop_columns(df, column_names):
    for i in column_names:
        df.drop(i, axis=1, inplace=True)
    return df

