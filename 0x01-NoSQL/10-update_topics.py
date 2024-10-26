#!/usr/bin/env python3
''' Task 10 '''


def update_topics(mongo_collection, name, topics):
    ''' Update all topics of collection's document based on name '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
