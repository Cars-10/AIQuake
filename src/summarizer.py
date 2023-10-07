# Create a function that takes in a dataframe and returs a dataframe with "Data type", "Unique values", "Missing value" as columns and the features as rows

import pandas as pd
import numpy as np

def summarize_dataframe(dataframe):
    dataframe_summary = pd.DataFrame({
        "Data type": dataframe.dtypes,
        "Unique values": dataframe.nunique(),
        "Missing value": dataframe.isnull().sum()
    })
    return dataframe_summary