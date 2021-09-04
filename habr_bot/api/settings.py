import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent
config_path = BASE_DIR / "config" / "config.yaml"


def read_config(path: str) -> dict:
    with open(path) as f:
        parsed_config = yaml.safe_load(f)
    return parsed_config


config = read_config(config_path)
