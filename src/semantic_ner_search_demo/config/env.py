#!/usr/bin/env python

from decouple import config
from unipath import Path

BASE_DIR = Path(__file__).parent

LOG_LEVEL = config("LOG_LEVEL", cast=str, default="WARNING")
DEFAULT_TZ = config("TZ", cast=str, default="Europe/London")

KAGGLE_USERNAME = config("KAGGLE_USERNAME", cast=str, default="")
KAGGLE_KEY = config("KAGGLE_KEY", cast=str, default="")

ES_CLOUD_ID = config("ES_CLOUD_ID", cast=str, default="")
ES_API_KEY = config("ES_API_KEY", cast=str, default="")

ELSER_MODEL_ID = config("ELSER_MODEL_ID", cast=str, default="")

ES_SEARCH_INDEX = config("ES_SEARCH_INDEX", cast=str, default="")
