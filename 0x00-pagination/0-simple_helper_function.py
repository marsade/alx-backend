#!/usr/bin/env python3
'''Simple helper function'''

def index_range(page: int, page_size: int) -> tuple:
    '''Specifies the corresponding range of pages in a list
    Args:
        page (int): The page number
        page_size (int): The size of each page
    Returns:
        tuple: The start and end indices for the given page
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
