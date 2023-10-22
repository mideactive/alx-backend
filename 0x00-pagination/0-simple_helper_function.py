#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
     Return a tuple of the start and
     end indexes based on page and page_size.
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
