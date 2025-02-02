#!/usr/bin/python
from base_caching import BaseCaching
'''Basic Caching dictionary'''


class BasicCache(BaseCaching):
    '''Basic dictionary caching'''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''Add an item in the cache'''
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
