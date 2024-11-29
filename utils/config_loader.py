import yaml


def load_config(file_path="config/config.yaml"):
    """
    Load configuration from a YAML file.
    :param file_path: Path to the YAML configuration file
    :return: Dictionary with configuration data
    """
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
