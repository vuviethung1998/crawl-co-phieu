from pymongo import MongoClient
import bson
import pandas as pd
import pytz
from datetime import datetime
import tzlocal

def convert_timestamp_in_datetime_utc(timestamp_received):
    local_timezone = tzlocal.get_localzone() # get pytz timezone
    return datetime.fromtimestamp(timestamp_received, local_timezone).strftime("%Y/%m/%d")

if __name__ == '__main__':
    MONGODB_URI = "mongodb://admin:admin@localhost:27017"
    MONGODB_DATABASE = 'CRAWLER_CO_PHIEU_FINANCE_STOCK'
    CRAWLER_COLLECTION = "LICH_SU_GIAO_DICH"

    connection = MongoClient(MONGODB_URI)
    db = connection[MONGODB_DATABASE]
    collection = db.database[CRAWLER_COLLECTION]
    cursor =  collection.find({})

    # write to json
    # with open('full_data.json', 'w') as file:
    #     file.write('[')
    #     for document in cursor:
    #         file.write(dumps(document, ensure_ascii=False))
    #         file.write(',')
    #     file.write(']')

    # write to csv
    lst_dict = []
    for doc in cursor:
        doc['Ngày Giao Dịch'] = convert_timestamp_in_datetime_utc(int(doc['Ngày Giao Dịch']) / 1000 )
        lst_dict.append(doc)

    df = pd.DataFrame(lst_dict)
    df.to_csv('output.csv', index=False)

