#!/usr/bin/env python3
"""Helper Function for pagination"""


def index_range(page, page_size):
    """Get the index range for a page

    Args:
        page (int): The page number whose index needs to be generated
        page_size (int): The data size of each page

    Returns:
        tuple: a pair of values representing the start and end index
    """

    end = page * page_size
    start = end - page_size

    return (start, end)
