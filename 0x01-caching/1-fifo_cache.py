#!/usr/bin/env python3
'''FIFO Caching'''
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''First-in-first-out caching'''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data = OrderedDict(self.cache_data)
            item = self.cache_data.popitem(last=False)
            print('DISCARD:', item[0])

    def get(self, key):
        '''Get an item by key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
