from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score, f1_score
import xgboost as xgb


####################################################################################################################

# FUNCTION THAT CALLS SELECTED MODEL (FOR NOW EITHER RANDOM FOREST OR XGBOOST)

def make_and_return_model(df_train_engineered, df_label_balanced):
    """Makes and returns a model for a dataframe with feature data and a dataframe with label data.

    Args:
        df_train_engineered (dataframe): The dataframe with feature data.
        df_label_balanced (dataframe): The dataframe with label data.

    Returns:
        model: The model.
    """

    # Test-train split
    X_train, X_test, y_train, y_test = train_test_split(df_train_engineered, df_label_balanced["damage_grade"], test_size=0.2, random_state=42, stratify= df_label_balanced["damage_grade"])

    return X_train, X_test, y_train, y_test, train_random_forest(X_train, y_train)

####################################################################################################################

# 1) RANDOM FOREST MODEL

def train_random_forest(X_train, y_train, n_estimators=100, random_state=42):
    """Train a Random Forest model and return it.

    Args:
        X_train (DataFrame): The feature data for training.
        y_train (Series): The labels for training.
        n_estimators (int): Number of trees in the forest.
        random_state (int): Random seed for reproducibility.

    Returns:
        RandomForestClassifier: The trained Random Forest model.
    """

    # Create and train the Random Forest model
    clf_rf = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    clf_rf.fit(X_train, y_train)

    return clf_rf

####################################################################################################################

# 2) XGBOOST MODEL

import xgboost as xgb

def train_xgboost(X_train, y_train, n_estimators=100, random_state=42):
    """Train an XGBoost model and return it.

    Args:
        X_train (DataFrame): The feature data for training.
        y_train (Series): The labels for training.
        n_estimators (int): Number of boosting rounds.
        random_state (int): Random seed for reproducibility.

    Returns:
        xgb.XGBClassifier: The trained XGBoost model.
    """

    # Subtract 1 from the labels to align with XGBoost's expectations
    y_train = y_train - 1

    # Create and train the XGBoost model
    clf_xgb = xgb.XGBClassifier(objective='multi:softprob', use_label_encoder=False, eval_metric='mlogloss', num_class=3, n_estimators=n_estimators, random_state=random_state)
    clf_xgb.fit(X_train, y_train)

    return clf_xgb


