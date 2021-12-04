import json
import os
from pathlib import Path
from urllib import parse

import pandas as pd
from pymongo import collection, MongoClient
from unidecode import unidecode

def get_mongo_connection(collection_name: str) -> collection.Collection:
    usr = parse.quote_plus(os.environ["MONGO_USER"])
    pwd = parse.quote_plus(os.environ["MONGO_PASS"])
    db_name = os.environ["MONGO_DB_NAME"]
    auth_source = os.environ["MONGO_AUTH_SOURCE"]
    host = os.environ["MONGO_HOST"]
    port = os.environ["MONGO_PORT"]

    conn_string = (f"mongodb://{usr}:{pwd}@{host}:{port}/{db_name}")
    mongo_client = MongoClient(conn_string)
    return mongo_client[db_name][collection_name]

def get_list_of_exams() -> list:
    exams_collection = get_mongo_connection("exams")
    returned_data = exams_collection.find({})
    exam_list = [{'data_series': x['data_series'], 'meta_fields': x['meta_fields']} for x in returned_data]
    return exam_list