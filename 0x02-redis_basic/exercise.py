#!/usr/bin/env python3
''' using the Redis NoSQL data storage '''
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


class Cache:
    ''' an object to store data in Redis data storage '''
    def __init__(self) -> None:
        ''' Initializes Cache instance '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store value in Redis data storage and returns the key '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        ''' Retrieve value from Redis data storage '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        ''' Retrieve string value from Redis data storage '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        ''' Retrieve integer value from Redis data storage  '''
        return self.get(key, lambda x: int(x))
