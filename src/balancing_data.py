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
                df_label_balanced (dataframe): The dataframe with balanced label data.
    """

    #     # Find the number of classes and the number of samples in each class
    #     n_classes = df_label["damage_grade"].nunique()

    #     # Find the class with the most samples
    #     max_samples = df_label["damage_grade"].value_counts().max()

    #     # Find the difference between the number of samples in the class with the most samples and the number of samples in each other class
    #     diff = max_samples - df_label["damage_grade"].value_counts()

    #     # Oversample each class with less samples than the class with the most samples
    #     for i in range(n_classes):
    #         # Print the number of samples in each class before oversampling
    #         df_train = df_train.append(
    #             df_train[df_label["damage_grade"] == i].sample(diff[i], replace=True)
    #         )
    #         df_label = df_label.append(
    #             df_label[df_label["damage_grade"] == i].sample(diff[i], replace=True)
    #         )
    #         # Print the number of samples in each class after oversampling
    #         print(
    #             "Number of samples in class {}: {}".format(
    #                 i, df_label["damage_grade"].value_counts()[i]
    #             )
    #         )

    #     # Shuffle the dataset
    #     df_train = df_train.sample(frac=1).reset_index(drop=True)
    #     df_label = df_label.sample(frac=1).reset_index(drop=True)

    return df_train, df_label
