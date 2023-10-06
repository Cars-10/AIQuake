from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


# With out numerical data frame "df_numerical" we want to implement a random forest model
def model01(X_train, y_train):
    """Makes and returns a model for a dataframe with feature data and a dataframe with label data.

    Args:
        df_train_engineered (dataframe): The dataframe with feature data.
        df_label_balanced (dataframe): The dataframe with label data.

    Returns:
        model: The model.
    """

    rf_model = RandomForestClassifier(criterion='gini',n_estimators=150,max_depth=4,n_jobs=-1)
    rf_model.fit(X_train, y_train)

    return rf_model


def make_and_return_model(df_train_engineered, df_label_balanced):
    """Makes and returns a model for a dataframe with feature data and a dataframe with label data.

    Args:
        df_train_engineered (dataframe): The dataframe with feature data.
        df_label_balanced (dataframe): The dataframe with label data.

    Returns:
        model: The model.
    """

    # Test-train split
    X_train, X_test, y_train, y_test = train_test_split(df_train_engineered, df_label_balanced["damage_grade"], test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, model02(X_train, y_train)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

def model02(X_train, y_train, n_estimators=100, random_state=42):
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
    clf = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    clf.fit(X_train, y_train)

    return clf