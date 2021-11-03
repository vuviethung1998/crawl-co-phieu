from pymongo import MongoClient

lst_cp= ['V12', 'PRC']

if __name__ == '__main__':
    MONGODB_URI = "mongodb://admin:admin@localhost:27017"
    MONGODB_DATABASE = 'CRAWLER_CO_PHIEU_TVSI'
    CRAWLER_COLLECTION = "CHI_TIEU_QUAN_TRONG"

    connection = MongoClient(MONGODB_URI)
    db = connection[MONGODB_DATABASE]
    collection = db.database[CRAWLER_COLLECTION]
    for cp in lst_cp:
        collection.remove({'Chung_khoan_name': cp})