import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent

dev_config_path = BASE_DIR / "config" / "config.yaml"
prod_config_path = BASE_DIR / "config" / "prod_config.yaml"


def read_config(path: str) -> dict:
    with open(path) as f:
        parsed_config = yaml.safe_load(f)
    return parsed_config


config = read_config(dev_config_path)
