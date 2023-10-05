import pandas as pd

def drop_columns(df, column_names: list):
    df_new = df.copy()
    df_new.drop(column_names, axis=1, inplace=True)

    return df_new

