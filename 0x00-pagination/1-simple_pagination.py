#!/usr/bin/env python3
import csv
import math
from typing import List


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
        '''Retrieves the list of pages
        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The size of each page. Defaults to 10.
        Returns:
            List[List]: The list of pages
        '''
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index < len(data) and end_index < len(data):
            return data[start_index:end_index]
        return []
