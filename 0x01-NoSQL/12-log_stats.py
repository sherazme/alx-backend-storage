#!/usr/bin/env python3
''' Task 12 '''
from pymongo import MongoClient


def print_request_logs(collection):
    '''Prints Nginx stats request logs '''
    print('{} logs'.format(collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = len(list(collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, count))
    checks_count = len(list(
        collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(checks_count))


def start():
    ''' Provides stats about Nginx logs '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_request_logs(client.logs.nginx)


if __name__ == '__main__':
    start()
