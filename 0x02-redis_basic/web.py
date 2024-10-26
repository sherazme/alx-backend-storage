#!/usr/bin/env python3
''' request caching and tracking '''
import redis
import requests
from functools import wraps
from typing import Callable


store = redis.Redis()
''' Redis instance '''


def data_cacher(method: Callable) -> Callable:
    ''' Caches output of fetched data '''
    @wraps(method)
    def invoke(url) -> str:
        ''' wrapper function '''
        store.incr(f'count:{url}')
        result = store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        store.set(f'count:{url}', 0)
        store.setex(f'result:{url}', 10, result)
        return result
    return invoke


@data_cacher
def get_page(url: str) -> str:
    ''' Returns HTML content of URL '''
    return requests.get(url).text
