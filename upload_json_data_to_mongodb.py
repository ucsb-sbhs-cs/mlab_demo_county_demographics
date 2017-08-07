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

def main():

    # parse command line arguments
    
    parser = argparse.ArgumentParser(
        description='upload json file to mlab database')
    
    parser.add_argument('jsonFile', type=str,
                    help='the file you want to upload')

    args = parser.parse_args()
	
	# connect to the MongoDB database

    url = os.environ["MONGO_URI"]
    
    client = pymongo.MongoClient(url)
    db = client[os.environ["MONGO_DBNAME"]]
    db.authenticate(os.environ["MONGO_USERNAME"],os.environ["MONGO_PASSWORD"])
    collection = db['counties']

    # read contents of the json file
    
    with open(args.jsonFile) as f:
        content = f.read()
        content_obj = json.loads(content)
        for c in content_obj:
            key = c["State"]+ " " + c["County"]
            key = key.replace(".", "")
            c["_id"] = key
            # insert it 
            object_id = collection.insert_one(c).inserted_id
    
    
        
if __name__=="__main__":
    main()
