#!/usr/bin/env python3

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import loading_data as ld

# ## Loading Data
df_train = ld.load_train_values()
df_label = ld.load_train_labels()
df_test = ld.load_test_values()

# integrate damage_grade into train_values
df_train['damage_grade'] = df_label['damage_grade']

print(df_train.shape)
print(df_label.shape)
print(df_test.shape)

# ## Data Exploration

# ### Finding the missing values


df_train_summary = pd.DataFrame({
    "Data type": df_train.dtypes,
    "Any nulls?": df_train.isnull().any(),
    "Unique values": df_train.nunique()
})
print(df_train_summary)

# Since there is no null, no data cleaning yet. (for rows)

# ## Data Preparation
# ### Balancing the data
import balancing_data as bd
df_train_balanced, df_label_balanced = bd.balance_dataset(df_train, df_label)

# ### Data Cleaning, Dropping the unnecessary columns, Encoding the categorical variables

import feature_engineering as fe
import geolocation_encoding as ge

df_geolocation_encoding, mean_damage_map = ge.encode_geolocation(
        df_train_balanced,
        df_label=df_label_balanced
        )
df_train_engineered = fe.engineer_features(df_geolocation_encoding)

# ### Feature Selection
df_train_engineered.info()


# ## 3. Modeling: Selection and Implementation
import models as md

X_train, X_test, y_train, y_test, rf_model = md.make_and_return_model(df_train_engineered, df_label_balanced)

# ## 4. Evaluation

# Predictions
preds = rf_model.predict(X_test)

# We want to evaluate our model with micro average f1 score
from sklearn.metrics import f1_score
f1_score(y_test, preds, average='micro')

# **Predictions**
#
# 01: 0.5682738243702155
#
# 02: 0.7203046756585638

# How is the model doing on each class?
from sklearn.metrics import classification_report
print(classification_report(y_test, preds))

# **NOTE: It's doing really bad on class 3, which is the second most common class.**

# ## 5. Predictions Output

# Preparing the predictions for the competition
# Format for the submission file (csv):
#
# building_id,damage_grade
# 11456,1
# 16528,1
# 3253,1
# 18614,1
# 1544,1
#
# (all numbers need to be integers!)
#
# Steps:
# * make a dataframe with the building_id
# * add the predictions to the dataframe (damage_grade)
# * make building_id the index
# * save to csv

# Doing the same preprocessing steps as we did for the training data
df_geolocation_encoding, _ = ge.encode_geolocation(df_test, mean_damage_map=mean_damage_map)
df_test_engineered = fe.engineer_features(df_geolocation_encoding, do_fit=False)

# dataframe with the building_id column
df_test_pred = df_test[['building_id']]

# Predictions adding to the dataframe
df_test_pred = df_test_pred.copy()
df_test_pred['damage_grade'] = rf_model.predict(df_test_engineered)

# making building_id the index
df_test_pred.set_index('building_id', inplace=True)

# Saving the dataframe to a csv file
df_test_pred.to_csv('../data/submission.csv')

# **Submissions**
#
# 01 by Johannes: 0.5683
