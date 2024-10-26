#!/usr/bin/env python3
''' Task 15's module '''
from pymongo import MongoClient
from collections import Counter


''' Connect to MongoDB '''
client = MongoClient("mongodb://localhost:27017/")
db = client['logs']
collection = db['nginx']

''' Query all logs '''
logs = collection.find()

''' Extract IPs from logs '''
ips = [log['ip'] for log in logs if 'ip' in log]

''' Count occurrences of each IP '''
ip_counter = Counter(ips)

''' Get the top 10 most common IPs '''
top_ips = ip_counter.most_common(10)

''' Print the results '''
print("Top 10 IPs:")
for ip, count in top_ips:
    print(f"{ip}: {count}")
