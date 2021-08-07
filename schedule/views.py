from django.shortcuts import render
from utils import get_db_handle, get_collection_handle

# Create your views here.
db_handle, mongo_client = get_db_handle(hope_db, )