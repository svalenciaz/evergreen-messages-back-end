from pymongo import MongoClient
from os import environ
from dotenv import load_dotenv
load_dotenv()

conn = MongoClient(environ.get('MONGO_URI'))
db = conn[environ.get('MONGO_DB')]