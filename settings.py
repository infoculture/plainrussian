from pathlib import Path

import environ

env = environ.Env(
    MONGO_HOST=(str, "localhost"),
    MONGO_PORT=(int, 27017),
    TEXTSBYGRADE_FOLDER=(str, "api/textmetric/textsbygrade"),
)
MONGO_HOST = env("MONGO_HOST")
MONGO_PORT = env("MONGO_PORT")
TEXTSBYGRADE_FOLDER = env("TEXTSBYGRADE_FOLDER")

BASE_DIR = Path(__file__).resolve().parent

