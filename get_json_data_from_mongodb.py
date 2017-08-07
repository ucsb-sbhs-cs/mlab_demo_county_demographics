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

import food_access

def main():

    # connect to the MongoDB database

    url = 'mongodb://{}:{}@{}:{}/{}'.format(
        os.environ["MONGO_USERNAME"],
        os.environ["MONGO_PASSWORD"],
        os.environ["MONGO_HOST"],
        os.environ["MONGO_PORT"],
        os.environ["MONGO_DBNAME"])
    
    client = pymongo.MongoClient(url)
    db = client[os.environ["MONGO_DBNAME"]]
    collection = db['food_access']

    # retrieve it

    document = collection.find_one()
    
    county_list = document["food_access"]

    states = food_access.get_states_list(county_list)
    print("states",states,"len(states)",len(states))

    CA_counties = food_access.get_counties_for_state(county_list,"CA")
    print("len(CA_counties)",len(CA_counties))

    CA_county_names = food_access.get_county_names_for_state(county_list,"CA")
    print("len(CA_county_names)",len(CA_county_names))
    print("CA_county_names",CA_county_names)

        
if __name__=="__main__":
    main()
