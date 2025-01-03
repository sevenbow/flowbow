"""Load and clean data, manage data streams and handle holdout splits.{% if cookiecutter.open_source_license != 'No license file' %}

{{ cookiecutter.open_source_license }}
Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author_name }}{% endif %}"""

from loguru import logger

from {{ cookiecutter.module_name }}.utils import read_tabular_data, write_tabular_data


def load_data(
    input_path,
    output_path = None,
):
    """Load and clean the raw dataset.

    Args:
        input_path (Path): Path to the raw dataset.
        output_path (Path, optional): Path to save the processed dataset. Defaults to None.

    Returns:
        DataFrame: Cleaned training dataset.
    """
    logger.info("Processing dataset...")

    ### Preprocessing START ###
    df = read_tabular_data(input_path)
    ### Preprocessing END ###

    logger.success("Processing dataset complete.")

    if output_path is not None:
        write_tabular_data(df, output_path)
    
    return df


if __name__ == "__main__":
    from {{ cookiecutter.module_name }}.config import config_logger, DATA_DIR
    config_logger()

    _ = load_data(DATA_DIR / "raw/dataset.csv", DATA_DIR / "processed/cleaned_train.csv")
