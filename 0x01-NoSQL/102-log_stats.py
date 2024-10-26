#!/usr/bin/env python3

from pymongo import MongoClient
from collections import Counter

def connect_to_mongo(uri="mongodb://localhost:27017/"):
    """
    Connects to the MongoDB server.

    Parameters:
        uri (str): The MongoDB connection URI.

    Returns:
        MongoClient: The MongoDB client.
    """
    return MongoClient(uri)

def fetch_logs(collection):
    """
    Fetches all logs from the specified MongoDB collection.

    Parameters:
        collection: The MongoDB collection to fetch logs from.

    Returns:
        list: A list of logs.
    """
    return collection.find()

def extract_ips(logs):
    """
    Extracts IP addresses from the logs.

    Parameters:
        logs (list): A list of log documents.

    Returns:
        list: A list of extracted IP addresses.
    """
    return [log['ip'] for log in logs if 'ip' in log]

def count_ips(ips):
    """
    Counts the occurrences of each IP address.

    Parameters:
        ips (list): A list of IP addresses.

    Returns:
        Counter: A Counter object with IP counts.
    """
    return Counter(ips)

def get_top_ips(ip_counter, top_n=10):
    """
    Retrieves the top N most common IP addresses.

    Parameters:
        ip_counter (Counter): A Counter object with IP counts.
        top_n (int): The number of top IPs to retrieve.

    Returns:
        list: A list of tuples containing top IPs and their counts.
    """
    return ip_counter.most_common(top_n)

def main():
    """
    Main function to execute the script.
    """
    # Connect to MongoDB
    client = connect_to_mongo()
    db = client['logs']
    collection = db['nginx']

    # Fetch logs and extract IPs
    logs = fetch_logs(collection)
    ips = extract_ips(logs)

    # Count IPs and get top 10
    ip_counter = count_ips(ips)
    top_ips = get_top_ips(ip_counter)

    # Print the results
    print("Top 10 IPs:")
    for ip, count in top_ips:
        print(f"{ip}: {count}")

if __name__ == "__main__":
    main()
