import pandas as pd

def drop_columns(df, column_names):
    return df.drop(columns=column_names)
