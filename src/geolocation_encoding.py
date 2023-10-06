def encode_geolocation(df, colomn_to_encode=['geo_level_3_id']):
    for col in colomn_to_encode:
        mean_damage = df.groupby(col)['damage_grade'].mean()
        df[str(col + '_mean_damage')] = df[col].map(mean_damage)
    return df