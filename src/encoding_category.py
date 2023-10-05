import pandas as pd

def encode_cat(df_train, df_test):
    # Identify categorical columns

    # Concatenate the train_values_df and test_values_df
    combined_df = pd.concat([df_train, df_test])

    # Get the categorical columns

    # Using ` .select_dtypes(include=[object]) ` to select columns with object
    # dtype which are the categorical columns in our case.
    categorical_columns = combined_df.select_dtypes(include=[object]).columns

    # Likewise, for numerical columns
    numerical_columns = combined_df.select_dtypes(exclude=[object]).columns

    # In Python, categorical columns are usually of type object.
    #categorical_columns, numerical_columns

    # One-hot encoding for categorical columns of train_values_df and test_values_df
    train_values_encoded_df = pd.get_dummies(df_train, columns=list(categorical_columns))
    test_values_encoded_df = pd.get_dummies(test_values_df, columns=list(categorical_columns))

    return train_values_encoded_df,test_values_encoded_df
