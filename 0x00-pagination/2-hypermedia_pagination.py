#!/usr/bin/env python3
"""A simple pagination"""
import csv
import math
from typing import List, Dict, Union


def index_range(page, page_size):
    """Get the index range for a page

    Args:
        page (int): The page number whose index needs to be generated
        page_isze (int): The data size of each page

    Returns:
        tuple: a pair of values representing the start and end index
    """
    assert page > 0
    assert page_size > 0

    end = page * page_size
    start = end - page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the page"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        page = data[start:end]
        return page

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List]]:
        """Get hypermedia data"""
        requested_page = self.get_page(page, page_size)
        len_data = len(self.dataset())
        total_pages = len_data // page_size
        remainder = len_data % page_size
        if remainder > 0:
            total_pages += 1
        hyper = {
            "page_size": page_size,
            "page": page,
            "data": requested_page,
            "next_page": None if page >= total_pages else page + 1,
            "prev_page": None if page == 1 else page - 1,
            "total_pages": total_pages
        }
        return hyper
