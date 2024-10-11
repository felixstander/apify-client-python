import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()

apify_config_path = Path(__file__).parent / "apify_config.yaml"

with open(apify_config_path, "r") as f:
    api_config = yaml.load(f, Loader=yaml.FullLoader)

apify_token = os.getenv("APIFY_TOKEN")

__all__ = ["api_config", "apify_token"]
