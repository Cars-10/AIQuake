import category_encoders as ce
import pandas as pd

# Defining lists with columns to be dropped
# First in the list is the building_id column, which is a unique identifier for each building. 
columns_to_drop = ['position', 'plan_configuration', 'legal_ownership_status']# ['building_id']

# This is a list of all categorical columns
# Comment out the columns that you don't want to drop. DO NOT DELETE ITEMS FROM THIS LIST.
categorical_columns = [
                       'land_surface_condition', 
                       'foundation_type', 
                       'roof_type', 
                       'ground_floor_type', 
                       'other_floor_type', 
                       'position', 
                       'plan_configuration', 
                       'legal_ownership_status'
                       ]

# This is a list of all numerical columns
columns_with_numbers = [
                        'geo_level_1_id', 
                        'geo_level_2_id', 
                        'geo_level_3_id', 
                        'count_floors_pre_eq', 
                        'age', 
                        'area_percentage', 
                        'height_percentage', 
                        'has_superstructure_adobe_mud', 
                        'has_superstructure_mud_mortar_stone', 
                        'has_superstructure_stone_flag', 
                        'has_superstructure_cement_mortar_stone', 
                        'has_superstructure_mud_mortar_brick', 
                        'has_superstructure_cement_mortar_brick', 
                        'has_superstructure_timber', 
                        'has_superstructure_bamboo', 
                        'has_superstructure_rc_non_engineered', 
                        'has_superstructure_rc_engineered', 
                        'has_superstructure_other', 
                        'count_families', 
                        'has_secondary_use', 
                        'has_secondary_use_agriculture', 
                        'has_secondary_use_hotel', 
                        'has_secondary_use_rental', 
                        'has_secondary_use_institution', 
                        'has_secondary_use_school', 
                        'has_secondary_use_industry', 
                        'has_secondary_use_health_post', 
                        'has_secondary_use_gov_office', 
                        'has_secondary_use_use_police', 
                        'has_secondary_use_other'
                        ]

# Combine the lists to drop columns
# columns_to_drop = columns_to_drop + categorical_columns #+ columns_with_numbers

# Categorical columns for one-hot encoding
columns_for_one_hot_encoding = [
                                'land_surface_condition', 
                                'foundation_type', 
                                'roof_type', 
                                'ground_floor_type', 
                                'other_floor_type'
                                ]
# columns_for_one_hot_encoding = None

# Categorical columns for base-n encoding
columns_for_base_n_encoding = categorical_columns
columns_for_base_n_encoding = None

# Function to drop columns from a dataframe
def drop_feature_columns(df, columns_to_drop=columns_to_drop):
    """Drops columns from a dataframe with feature data.
    
    Args:
        df (dataframe): The dataframe to drop columns from.
        columns_to_drop (list): A list of columns to drop.
    
    Returns:
        df (dataframe): The dataframe with dropped columns.
    """

    print(f'Dropping {len(columns_to_drop)} columns from the dataframe.')
    print('List of columns to drop:')
    for idx, column in enumerate(columns_to_drop):
        print(f'{idx}:\t{column}')
    print('')
    return df.drop(columns_to_drop, axis=1)

# Function for categorical encoding
encoder_one_hot = ce.OneHotEncoder()
encoder_base_n = ce.BaseNEncoder(base=3)
def encode_categorical(df, 
                       columns_for_one_hot_encoding=columns_for_one_hot_encoding, 
                       columns_for_label_encoding=None,
                       columns_for_base_n_encoding=columns_for_base_n_encoding,
                       columns_for_binary_encoding=None,
                       do_fit=True):
    """Encodes categorical columns for a dataframe with feature data.
    
    Args:
        df (dataframe): The dataframe to encode categorical columns for.
        columns_for_one_hot_encoding (list): A list of columns for one-hot encoding.
        columns_for_label_encoding (list): A list of columns for label encoding.
        columns_for_base_n_encoding (list): A list of columns for base-n encoding.
        columns_for_binary_encoding (list): A list of columns for binary encoding.
    
    Returns:
        df (dataframe): The dataframe with encoded categorical columns.
    """

    df_out = df.copy()
    # Identify categorical columns
    if columns_for_one_hot_encoding is not None:
        global encoder_one_hot
        # One-hot encoding for categorical columns in columns_for_one_hot_encoding 
        # using OneHotEncoder from category_encoders
        print(f'One-hot encoding {len(columns_for_one_hot_encoding)} columns.')
        print('List of columns to one-hot encode:')
        for idx, column in enumerate(columns_for_one_hot_encoding):
            print(f'{idx}:\t{column}')
        print('')

        if do_fit:
            pass
            # Fit the encoder_one_hot on the dataframe
            # encoder_one_hot.fit(df_out, cols=columns_for_one_hot_encoding)

        # Use the encoder_one_hot to transform the dataframe
        # df_out = encoder_one_hot.transform(df_out)
        df_out = pd.get_dummies(df_out, columns=columns_for_one_hot_encoding)
        

    if columns_for_label_encoding is not None:
        pass

    if columns_for_base_n_encoding is not None:
        # Base N encoding with base 3
        # using BaseNEncoder from category_encoders
        print(f'Base N encoding {len(columns_for_base_n_encoding)} columns.')
        print('List of columns to base N encode:')
        for idx, column in enumerate(columns_for_base_n_encoding):
            print(f'{idx}:\t{column}')
        print('')

        if do_fit:
            # Fit the encoder_base_n on the dataframe
            encoder_base_n.fit(df_out, cols=columns_for_base_n_encoding)

        # Use the encoder_base_n to transform the dataframe
        df_out = encoder_base_n.transform(df_out)

    if columns_for_binary_encoding is not None:
        pass

    # One-hot encoding for categorical columns
    return df_out

# Function for feature engineering
def engineer_features(df, do_fit=True):
    """Engineers features for a dataframe with feature data.
    
    Args:
        df (dataframe): The dataframe to engineer features for.
    
    Returns:
        df (dataframe): The dataframe with engineered features.
    """
    # Drop columns
    df = drop_feature_columns(df)

    # Encode categorical columns
    df = encode_categorical(df, do_fit=do_fit)

    if False:
        # Print information about the dataframe
        print('Dataframe info:')
        print(df.info())
        print('')
        print('Dataframe head:')
        print(df.head())
        print('')
        print('Dataframe desciption:')
        print(df.describe())

        global df_label
        # Show the correlation of the features in df with the target in df_label
        print('Correlation of features with target:')
        print(df.corrwith(df_label["damage_grade"]))




    # Return the dataframe with engineered features
    return df