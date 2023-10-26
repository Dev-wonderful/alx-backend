#!/usr/bin/python3
""" MRU Caching module
"""
from base_caching import BaseCaching
"""
The difference between MRU and LIFO is that MRU updates the queue when
you get or put an item unlike LIFO which only updates the queue when you put
the item into the cache. If the item already exists in the queue it won't
be moved to the back of the queue, unlike LIFO which would move the item
to the back of the queue. MRU would only move the item to the back of the
queue when you access the item's data
"""


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - Most Recently Used algorithm for your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.mru_queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                discard = self.mru_queue.pop(-1)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            if key not in self.mru_queue:
                self.mru_queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if self.cache_data.get(key):
            if key in self.mru_queue:
                self.mru_queue.remove(key)
            self.mru_queue.append(key)
            # print(self.mru_queue)
        return self.cache_data.get(key, None)
