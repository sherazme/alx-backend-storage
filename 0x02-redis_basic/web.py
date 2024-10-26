#!/usr/bin/env python3
''' request caching and tracking '''
import redis
import requests
from functools import wraps
from typing import Callable


store = redis.Redis()
''' Redis instance '''


def count_access(method):
    """ Decorator counts URL access times """
    @wraps(method)
    def wrapper(url):
        key = "cached:" + url
        data = store.get(key)
        if data:
            return data.decode("utf-8")

        key = "count:" + url
        html = method(url)

        store.incr(key)
        store.set(key, html)
        store.expire(key, 10)
        return html
    return wrapper


@count_access
def get_page(url: str) -> str:
    ''' Returns HTML content of URL '''
    return requests.get(url).text
