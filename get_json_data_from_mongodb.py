#!/usr/bin/env python
# Quick script to upload a JSON file to a MongoDB database,
# e.g. one provided on the free tier of mlab.com

# Documentation about pymongo can be found here:
#    http://api.mongodb.com/python/current/tutorial.html

# Phill Conrad (UCSB) / Sky Adams (SBHS)
# 06/26/2017

import argparse
import pymongo
import json
import os
import sys

import pprint


def main():

    # connect to the MongoDB database

    url = os.environ["MONGO_URI"]
    
    client = pymongo.MongoClient(url)
    db = client[os.environ["MONGO_DBNAME"]]
    db.authenticate(os.environ["MONGO_USERNAME"],os.environ["MONGO_PASSWORD"])
    collection = db['counties']

    # retrieve it

    document = collection.find_one({'_id':"CA Santa Barbara County"})
    pprint.pprint(document)
        
if __name__=="__main__":
    main()
