"""Train a model and compute evaluation metrics."""

import numpy as np
from loguru import logger
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import get_scorer

from {{ cookiecutter.module_name }}.models import build_model, save_model
from {{ cookiecutter.module_name }}.utils import read_tabular_data


def train(
    X,
    y,
    model_params=None,
    cv=5, # can also use train-test
    metrics=[],
    model_path=None
):
    """Train a model and compute evaluation metrics.

    This function is supposed to do four things in order:
    1. Perform training along with the validation setup.
    2. Evaluate the model on specified metrics.
    3. Retrain the model on the full dataset.
    4. Save the model if a path is provided.

    Args:
        X (DataFrame): Features.
        y (DataFrame): Labels.
        model_params: Model parameters.
        cv (int, optional): Number of cross-validation folds. Defaults to 5.
        eval_metrics (list, optional): Evaluation metrics to compute. Defaults to [].
        model_path: Path to save the model. Defaults to None.

    Returns:
        object: Trained model.
        np.ndarray: Out-of-fold predictions.
        dict: Evaluation metrics.
    """
    # Perform CV
    skf = StratifiedKFold(cv)
    scorers = {metric: get_scorer(metric)._score_func for metric in metrics}

    train_scores = {metric:[] for metric in metrics}
    valid_scores = {metric:[] for metric in metrics}
    oof_preds = np.zeros(len(y), dtype=int)
    models = []
    for fold, (tridx, validx) in enumerate(skf.split(X, y)):
        model_ = build_model(model_params)
        
        model_.fit(
            X[list(tridx)].to_numpy(),
            y[list(tridx)].to_numpy().ravel(),
        )
        models.append(model_)

        y_pred = model_.predict(X[list(validx)].to_numpy())
        oof_preds[validx] = y_pred

        for metric in metrics:
            valid_score = scorers[metric](y[list(validx)].to_numpy().ravel(), y_pred)
            valid_scores[metric].append(valid_score)

            train_score = scorers[metric](y[list(tridx)].to_numpy().ravel(), model_.predict(X[list(tridx)].to_numpy()))
            train_scores[metric].append(train_score)

            logger.info(f"Fold: {fold+1}/{cv}, Train {metric}: {train_score}, Valid {metric}: {valid_score}")

    # Compute CV mean and standard deviation of train and valid scores
    cv_mean_train_scores = {metric: np.mean(train_scores[metric]) for metric in metrics}
    cv_std_train_scores = {metric: np.std(train_scores[metric]) for metric in metrics}
    cv_mean_valid_scores = {metric: np.mean(valid_scores[metric]) for metric in metrics}
    cv_std_valid_scores = {metric: np.std(valid_scores[metric]) for metric in metrics}

    # Compute OOF scores
    oof_score = {metric: scorers[metric](y, oof_preds) for metric in metrics}

    evaluation_metrics = {
        "CV Mean Train score": cv_mean_train_scores,
        "CV Std Train score": cv_std_train_scores,
        "CV Mean Valid score": cv_mean_valid_scores,
        "CV Std Valid score": cv_std_valid_scores,
        "OOF Score": oof_score,
    }

    # Retrain model on full dataset
    model = build_model(model_params)
    model.fit(X.to_numpy(), y.to_numpy().ravel())

    # Save model
    if model_path is not None:
        save_model(model, model_path)
        logger.info(f"Model saved to {model_path}")

    return model, oof_preds, evaluation_metrics


if __name__=="__main__":
    from {{ cookiecutter.module_name }}.config import config_logger, DATA_DIR, ARTIFACTS_DIR
    config_logger()

    # Load feature cols
    with open(DATA_DIR / "processed/feature_cols.txt", "r") as f:
        feature_cols = f.read().splitlines()
    
    # Load dataset
    target_col = "AFib_Label" ## REPLACE THIS
    train_data = read_tabular_data(DATA_DIR / "processed/train_features.csv")
    X = train_data[feature_cols]
    y = train_data[target_col]

    # Train model
    cv = 5  ## REPLACE THIS
    train(
        X,
        y,
        model_params=None,
        cv=cv,
        metrics=["f1_score"],
        model_path=ARTIFACTS_DIR / "models/model.pkl"
    )
