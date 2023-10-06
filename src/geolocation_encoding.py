def encode_geolocation(
    df,
    colomn_to_encode=[
        #'geo_level_3_id',
        "geo_level_1_id",
        "geo_level_2_id",
    ],
    mean_damage_maps=None,
    df_label=None,
):
    if mean_damage_maps is None:
        df["damage_grade"] = df_label["damage_grade"]
        mean_damage_maps = {}
        for col in colomn_to_encode:
            mean_damage_map = df.groupby(col)["damage_grade"].mean()
            # save mean_damage_map
            mean_damage_maps[col] = mean_damage_map
            df[str(col + "_mean_damage")] = df[col].map(mean_damage_map)
        df = df.drop(columns=["damage_grade"])
        return df, mean_damage_maps
    else:
        for col in colomn_to_encode:
            df[str(col + "_mean_damage")] = df[col].map(mean_damage_maps[col])
            # Count the NaN values in the column and print the result
            n_NaN = df[str(col + "_mean_damage")].isna().sum()
            print(
                "{} column has {} NaN values, which getting filled with mean {}".format(
                    str(col + "_mean_damage"), n_NaN, mean_damage_maps[col].mean()
                )
            )
            # For all NaN values, replace with the mean damage grade
            df[str(col + "_mean_damage")] = df[str(col + "_mean_damage")].fillna(
                mean_damage_maps[col].mean()
            )
        return df, mean_damage_maps
