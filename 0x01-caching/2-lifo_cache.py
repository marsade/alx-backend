#!/usr/bin/env python3
'''LIFO Caching'''
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    '''LIFO Caching Class Implementation'''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        if len(self.cache_data) >= self.MAX_ITEMS:
            lifo_key, lifo_item = self.cache_data.popitem()
            print('DISCARD:', lifo_key)
        self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
