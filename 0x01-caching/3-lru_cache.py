#!/usr/bin/python3
""" LRU Caching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - Last Recently Used algorithm for your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.lru_queue = []
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key not in self.queue:
                self.queue.append(key)
                self.lru_queue.append(key)
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                len_lru = len(self.lru_queue)
                if len_lru > 0:
                    discard_list = [item for item in self.queue
                                    if item not in self.lru_queue]
                    if len(discard_list) > 0:
                        discard = discard_list.pop(0)
                    else:
                        discard = self.lru_queue.pop(0)
                    self.queue.remove(discard)

                else:
                    discard = self.queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Get an item by key
        """
        if self.cache_data.get(key):
            if key in self.lru_queue:
                self.lru_queue.remove(key)
            self.lru_queue.append(key)
        return self.cache_data.get(key, None)
