"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    idict.py

    Immutable dictionary
"""

import collections


class IDict(collections.Mapping):
    """
    IDict

    Dynamic Immutable/Mutable dictionary class,
    can be used as a normal dictionary but can be __immutable or mutable
    set in the constructor.
    """

    def __init__(self, immutable: bool = True, *args, **kwargs):
        """
        sets the input dictionary passed through and makes it __immutable or
        mutable based on the input param '__immutable' (True/False)

        :param immutable: set to True to make this dict __immutable, ow. is mutable
        :param args: input args
        :param kwargs: input dict args
        """
        self._d = dict(*args, **kwargs)
        self._hash = None
        self.__immutable = immutable

    def __iter__(self):
        """
        returns iterable object of dictionary

        :return:
        """
        return iter(self._d)

    def __len__(self):
        """
        returns length of dictionary

        :return:
        """
        return len(self._d)

    def __getitem__(self, key):
        """
        gets item from index key

        :param key: index key
        :return: value from dictionary as per key
        """
        return self._d[key]

    def __hash__(self):
        """
        updates and returns hash value of all items in the dictionary

        :return:
        """
        if self._hash is None:
            hash_ = 0
            for pair in self.items():
                hash_ ^= hash(pair)
            self._hash = hash_
        return self._hash

    def __setitem__(self, key, value):
        """
        sets items in dictionary if dictionary is mutable
        checks self.__immutable (bool)

        :param key: key index to set
        :param value: value to set
        :return:
        """
        if not self.__immutable:
            self._d[key] = value
        else:
            raise TypeError("object is __immutable (set to False), "
                            "cannot set assignment in this object.")

    @property
    def is_immutable(self) -> bool:
        """
        returns True if this dict obj is immutable, otherwise false
        :return: looks at self.__immutable, set in the constructor
        """
        return self.__immutable
