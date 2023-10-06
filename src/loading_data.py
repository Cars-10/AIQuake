import pandas as pd

def load_train_values():
    """Loads the train data from the data directory.

    Returns:
        train_data (dataframe): A list of the test data.
    """
    return pd.read_csv('../data/train_values.csv')

def load_train_labels():
    """Loads the train labels from the data directory.

    Returns:
        train_labels (dataframe): A list of the test labels.
    """
    return pd.read_csv('../data/train_labels.csv')

def load_test_values():
    """Loads the test data from the data directory.

    Returns:
        test_data (dataframe): A list of the test data.
    """
    return pd.read_csv('../data/test_values.csv')