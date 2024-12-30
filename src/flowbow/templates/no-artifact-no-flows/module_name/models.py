"""Core model building engine.

{% if is_license %}
{{ license }} License ({{ license_url }})
Copyright (c) {{ year }} {{ author_name }}
{% endif %}
"""


def build_model(model_config):
    """Build model given the configuration.

    Args:
        model_config: Model configuration

    Returns:
        model
    """
    pass


def save_model(model, path):
    pass


def load_model(path):
    pass