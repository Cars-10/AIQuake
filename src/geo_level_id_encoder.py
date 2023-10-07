import pandas as pd

def encode_geolocation(df_train, df_test, columns_to_encode):
    mean_damage_maps = {}
    
    # Concatenate train and test data to ensure consistent encoding
    combined_data = pd.concat([df_train, df_test], ignore_index=True)

    for col in columns_to_encode:
        # Calculate mean damage map for combined data (train + test)
        mean_damage_map = combined_data.groupby(col)["damage_grade"].mean()
        # Save mean_damage_map
        mean_damage_maps[col] = mean_damage_map

        # Apply mean encoding to the training data
        df_train[str(col + "_mean_damage")] = df_train[col].map(mean_damage_map)

        # Apply mean encoding to the testing data
        df_test[str(col + "_mean_damage")] = df_test[col].map(mean_damage_map)
        
        # Fill missing values in the testing data with the mean damage grade from training data
        df_test[str(col + "_mean_damage")].fillna(
            df_train[str(col + "_mean_damage")].mean(), inplace=True
        )

    return df_train, df_test, mean_damage_maps
