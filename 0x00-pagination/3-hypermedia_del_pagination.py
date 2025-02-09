#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Retrieves indexed hypermedia pagination
            Args:
            index (int, optional): The index of the data. Defaults to None.
            page_size (int, optional): The size of each page. Defaults to 10.
            Returns:
                Dict: The indexed hypermedia response
        '''
        dataset = self.indexed_dataset()
        data_len = len(dataset)
        assert 0 <= index <= data_len
        next_index = index if dataset.get(index) else None
        data = []
        for _ in range(page_size):
            while True:
                ele = dataset.get(index)
                index += 1
                if ele is not None:
                    break
            data.append(ele)
        return {
            "index": index,
            "data": data,
            "next_index": next_index,
            "page_size": len(data)
        }
