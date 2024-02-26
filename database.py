"""This module provides functionality for connecting to a MongoDB database."""
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/db")

db = client.library
