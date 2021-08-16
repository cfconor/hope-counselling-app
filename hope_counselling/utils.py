from pymongo import MongoClient

def db_connector():
    client = MongoClient('mongodb+srv://hopeadmin:RedHouse1!@cluster0.zciqo.mongodb.net/hope_db?retryWrites=true&w=majority')
    db = client['hope_db']

    return client, db