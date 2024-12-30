"""Data preprocessing, transformation, imputation, and feature engineering.

{% if is_license %}
{{ license }} License ({{ license_url }})
Copyright (c) {{ year }} {{ author_name }}
{% endif %}
"""


def feature_engineering_train(df):
    """Create feature training set.

    Args:
        df (DataFrame): Cleaned dataframe.

    Returns:
        DataFrame: Preprocessed dataframe where `feature_cols` are ready for modeling.
        feature_cols: Feature columns to be used for modeling
        artifacts: Generated artifacts like mean/std values, one hot encoder, etc.
    """
    pass


def feature_engineering_test(df, artifacts):
    """Create feature holdout set.

    Args:
        df (DataFrame): Cleaned dataframe.
        artifacts (dict[str, Any]): Artifacts if any; that were generated to process training dataset.

    Returns:
        DataFrame: Preprocessed dataframe.
    """
    pass
