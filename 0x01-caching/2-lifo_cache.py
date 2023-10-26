#!/usr/bin/python3
""" LIFO Caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - Last In, First out algorithm for your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                discard = self.queue.pop(3)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
