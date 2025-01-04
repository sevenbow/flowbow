#!/usr/bin/env python3
"""Entrypoint script to run flows and anything easily through commands.

Usage example:

```bash
# Prepare training data
python main.py prepare-train-data

# Use --help to see all options
python main.py --help
```
"""

import typer
import hydra
from omegaconf import OmegaConf
from metaflow import Runner
from rich import print

app = typer.Typer()


def get_cfg():
    hydra.initialize("config", version_base=None)
    cfg = OmegaConf.to_container(hydra.compose(config_name="train"))
    return cfg


@app.command()
def prepare_train_data():
    """Run flow to prepare training data"""
    cfg = get_cfg()
    with Runner("cmipiu/flows/prepare_train_data.py").run(
        config=cfg
    ) as running:
        print(f"{running.run} completed")


@app.command()
def prepare_test_data():
    """Run flow to prepare testing data"""
    cfg = get_cfg()
    with Runner("cmipiu/flows/prepare_test_data.py").run(config=cfg) as running:
        print(f"{running.run} completed")


@app.command()
def train():
    """Run flow to train all the models"""
    cfg = get_cfg()
    with Runner("cmipiu/flows/train_ml_models.py").run(config=cfg) as running:
        print(f"{running.run} completed")


@app.command()
def predict():
    """Run inference flow"""
    with Runner("cmipiu/flows/predict_sii.py").run() as running:
        print(f"{running.run} completed")

if __name__ == "__main__":
    app()