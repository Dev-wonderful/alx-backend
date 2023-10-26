#!/usr/bin/python3
""" MRU Caching module
"""
from base_caching import BaseCaching


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
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key not in self.queue:
                self.queue.append(key)

            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                len_mru = len(self.mru_queue)
                if len_mru > 0:
                    discard_list = [item for item in self.queue
                                    if item in self.mru_queue]
                    if len(discard_list) > 0:
                        discard = discard_list.pop(-1)
                        self.mru_queue.remove(discard)
                    else:
                        discard = self.mru_queue.pop(-1)
                    self.queue.remove(discard)

                else:
                    discard = self.queue.pop(-1)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
                # self.mru_queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if self.cache_data.get(key):
            if key in self.mru_queue:
                self.mru_queue.remove(key)
            self.mru_queue.append(key)
            print(self.mru_queue)
        return self.cache_data.get(key, None)
