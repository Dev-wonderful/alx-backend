#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BaseCache defines:
      - algorithm of your caching system
      - where your data are stored (in a dictionary)
    """
   
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
