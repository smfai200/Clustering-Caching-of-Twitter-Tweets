import os
import pandas as pd
from Caching.models import *
import os
import numpy as np

def Read_h5():
    datadir = os.path.realpath('../data')
    with pd.HDFStore(os.path.join(datadir, 'results.h5')) as store:
        tweets = store.results

    return tweets

def read_vocab():
    vocab_idf = pd.read_csv("../data/results/TFIDF_SparseMatrix.csv")
    return vocab_idf

# def SavetoDB_new(data):
#     data.fillna(0, inplace=True)
#     data["timeStamp"].astype(str)
#     row_iter = data.iterrows()
#     for index, row in row_iter:
#         try:
#             Data(
#                 lat=row['lat'],
#                 lng=row['lng'],
#                 text=row['text'],
#                 timeStamp=row['timeStamp'],
#                 user_id=row['user_id'],
#                 mb_cluster=row['mb_cluster'],
#                 db_cluster=row['db_cluster'],
#                 cluster=row['cluster'],
#             ).save()
#             print("Processed")
#         except:
#             pass
#
# def Run(option):
#     df = Read_h5()
#     vocab_idf = read_vocab()
#     if(option == "KMEANS"):
#         SavetoDB_new(df["mb_cluster"])
#     elif(option == "DBSCAN"):
#         SavetoDB_new(df["db_cluster"])
#     elif(option == "HDBSCAN"):
#         SavetoDB_new(df["hdb_cluster"])


def SavetoDB():
    datadir =  os.path.realpath('../results')
    files = os.listdir(datadir)
    print(files[:5])
    for file in files:
        print("Processing ", file)
        data = pd.read_csv(os.path.join(datadir,file), engine='python')
        data.fillna(0, inplace=True)
        data["timeStamp"].astype(str)
        row_iter = data.iterrows()
        for index,row in row_iter:
            try:
                Data(
                    lat=row['lat'],
                    lng=row['lng'],
                    text=row['text'],
                    timeStamp=row['timeStamp'],
                    user_id=row['user_id'],
                    mb_cluster=row['mb_cluster'],
                    db_cluster=row['db_cluster'],
                    cluster=row['cluster'],
                ).save()
                print("Processed")
            except:
                pass
