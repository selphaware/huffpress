"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    imdict.py

    Immutable dictionary
"""

import collections


class ImDict(collections.Mapping):
    """
    ImDict

    Immutable dictionary class, can be used as a normal dictionary but
    is immutable.
    """

    def __init__(self, *args, **kwargs):
        self._d = dict(*args, **kwargs)
        self._hash = None

    def __iter__(self):
        return iter(self._d)

    def __len__(self):
        return len(self._d)

    def __getitem__(self, key):
        return self._d[key]

    def __hash__(self):
        if self._hash is None:
            hash_ = 0
            for pair in self.items():
                hash_ ^= hash(pair)
            self._hash = hash_
        return self._hash
