import os
from pathlib import Path

from dotenv import load_dotenv


class Settings:
    def __init__(self):
        self.dev_mode = None

    def load_config(self, env_file: Path):
        load_dotenv(env_file, override=True)
        self.dev_mode = os.getenv("DEV") in ["True", "TRUE"]


settings = Settings()
