#!/usr/bin/env python3


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of the start and end
    indexes based on page and page_size.
    """
    # Calculate the start index (0-based)
    start = (page - 1) * page_size

    # Calculate the end index
    end = start + page_size

    return (start, end)


# Testing the function
if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
