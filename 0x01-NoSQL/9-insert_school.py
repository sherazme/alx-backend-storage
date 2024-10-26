#!/usr/bin/env python3
''' Task 9 '''


def insert_school(mongo_collection, **kwargs):
    ''' Inserts new document in collection '''
    r = mongo_collection.insert_one(kwargs)
    return r.inserted_id
