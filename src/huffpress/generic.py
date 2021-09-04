"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    generic.py

    Contains generic functionality (converting decimal <-> binary), and the
    compression modes
"""

from enum import Enum
from typing import List


def dec_to_bin(num: int) -> List[int]:
    """
    dec_to_bin(num: int) -> List[int]:

    Convert decimal to binary list

    :param num: decimal number
    :return: binary list of 1's 0's
    """
    out_bin = []
    while num > 0:
        out_bin += [num % 2]
        num //= 2
    out_bin.reverse()
    return out_bin


def bin_to_dec(in_bin: List[int]) -> int:
    """
    bin_to_dec(in_bin: List[int]) -> int:

    Convert binary list to decimal integer

    :param in_bin: binary list of 1's and 0's
    :return: decimal integer converted from input binary
    """
    in_bin.reverse()
    res = 0
    for i, x in enumerate(in_bin):
        res += x * (2 ** i)
    return res


class Mode(Enum):
    """
    Compression modes

    0 - Default (File or Raw input data)
    1 - File compression only
    2 - Raw input data compression only
    """
    DEFAULT = 0
    FILE = 1
    RAW = 2
