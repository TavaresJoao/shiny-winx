import json
import os
from pathlib import Path
from urllib import parse
from datetime import datetime
import dateutil.parser

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
    exam_list = [{'date_series': x['date_series'], 'meta_fields': x['meta_fields']} for x in returned_data]
    return exam_list

def insert_one_exam(exam_data) -> bool:
    to_add = dict()
    to_add['date_series'] = dict()
    to_add['date_series']['dt'] = list()
    to_add['date_series']['pt'] = list()
    to_add['meta_fields'] = exam_data.meta_fields

    assert len(exam_data.date_series['dt']) == len(exam_data.date_series['pt'])

    for dt, pt in zip(exam_data.date_series['dt'], exam_data.date_series['pt']):
        to_add['date_series']['dt'].append(dateutil.parser.parse(dt))
        to_add['date_series']['pt'].append(float(pt))

    exams_collection = get_mongo_connection("exams")
    exams_collection.insert_one(to_add)

    return True

def login_medic(login_data) -> dict:
    doctors_collection = get_mongo_connection("Doctors")
    login_query = {"username": login_data.username, "password": login_data.password}
    tentalogin = doctors_collection.find(login_query)
    try:
        return [{'name': x['name'], 'CRM': x['crm'], 'token': 'abc'} for x in tentalogin]
    except Exception as e:
        return None
    