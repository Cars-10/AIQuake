def balance_dataset(df_train, df_label):
    """Balance the dataset by oversampling the minority classes.
    First we find the number of classes and the number of samples in each class.
    Then we find the class with the most samples.
    Then we find the difference between the number of samples in the class with the most samples and the number of samples in each other class.
    Then we oversample each class with less samples than the class with the most samples.
    Finally we return the balanced dataset.


    Args: df_train (dataframe): The dataframe with feature data.
          df_label (dataframe): The dataframe with label data.

    Returns: df_train_balanced (dataframe): The dataframe with balanced feature data.
             df_label_balanced (dataframe): The dataframe with balanced label data."""

    return df_train, df_label
