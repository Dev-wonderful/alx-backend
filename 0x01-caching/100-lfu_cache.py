#!/usr/bin/python3
""" LFU Caching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - Last Frequently Used algorithm for your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.lfu_record = []
        self.queue = []
        # self.MAX_ITEMS = 1

    def update_record_frequency(self, key):
        """Update the data frequency and the record arrangement"""
        for index, record in enumerate(self.lfu_record):
            if key == record['key']:
                record['freq'] += 1
                if len(self.lfu_record) == 1:
                    return
                item = self.lfu_record.pop(index)
                break
        for index, record in enumerate(self.lfu_record):
            if record['freq'] < item['freq']:
                self.lfu_record.insert(index, item)
                break
            elif index == len(self.lfu_record) - 1:
                self.lfu_record.append(item)
                break

    def put(self, key, item):
        """ Add an item in the cache
        """
        data = {
            'key': '',
            'freq': 0
        }
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                lfu_info = {
                    'min': self.lfu_record[0].get('freq'),
                    'index': 0
                }
                # duplicate: int
                for index, record in enumerate(self.lfu_record):
                    if lfu_info['min'] > record['freq']:
                        lfu_info['min'] = record['freq']
                        lfu_info['index'] = index
                discard = self.lfu_record.pop(lfu_info['index'])
                self.queue.remove(discard.get('key'))
                del self.cache_data[discard.get('key')]
                print("DISCARD: {}".format(discard.get('key')))
            if key not in self.queue:
                self.queue.append(key)
                data['key'] = key
                self.lfu_record.append(data)
            else:
                self.update_record_frequency(key)
            # print(f"record: {self.lfu_record}")

    def get(self, key):
        """ Get an item by key
        """
        if self.cache_data.get(key):
            # print(f"record: {self.lfu_record}")
            # print(f"key: {key}")
            if key in self.queue:
                self.queue.remove(key)
                self.update_record_frequency(key)
            self.queue.append(key)
            # print(f"record: {self.lfu_record}")
        return self.cache_data.get(key, None)
