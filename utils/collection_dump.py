from pymongo import MongoClient
import bson
import pandas as pd
import pytz
from datetime import datetime
# import tzlocal

# def convert_timestamp_in_datetime_utc(timestamp_received):
#     local_timezone = tzlocal.get_localzone() # get pytz timezone
#     return datetime.fromtimestamp(timestamp_received, local_timezone).strftime("%Y/%m/%d")

def convertColumnToNumeric(col):
    if type(col) == str:
        return float(col.replace(',', ''))
    return col


if __name__ == '__main__':
    MONGODB_URI_1 = "mongodb://admin:admin@localhost:27018"
    MONGODB_DATABASE_1 = 'CRAWLER_CO_PHIEU_CAFEF'
    CRAWLER_COLLECTION_1 = "THONG_KE_DAT_LENH"

    MONGODB_URI_2 = "mongodb://admin:admin@202.191.57.62:27018"
    MONGODB_DATABASE_2 = 'CRAWLER_CO_PHIEU_CAFEF'
    CRAWLER_COLLECTION_2 = "THONG_KE_DAT_LENH"

    connection_1 = MongoClient(MONGODB_URI_1)
    db_1 = connection_1[MONGODB_DATABASE_1]
    collection_1 = db_1.database[CRAWLER_COLLECTION_1]
    cursor_1 =  collection_1.find({})

    connection_2 = MongoClient(MONGODB_URI_2)
    db_2 = connection_2[MONGODB_DATABASE_2]
    collection_2 = db_2.database[CRAWLER_COLLECTION_2]

    # ------------------------------------
    # normalize chi tieu quan trong
    for item in cursor_1:
        # doc['Ngày Giao Dịch'] = convert_timestamp_in_datetime_utc(int(doc['Ngày Giao Dịch']) / 1000 )
        if collection_2.count_documents({'Chung_khoan_name':item['Chung_khoan_name'],'Ngày':item['Ngày']}, limit = 1):
            print('Item existed!')
        else:
            collection_2.insert(item)