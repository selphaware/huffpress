from enum import Enum


def dec_to_bin(num: int):
    out_bin = []
    while num > 0:
        out_bin += [num % 2]
        num //= 2
    out_bin.reverse()
    return out_bin


def bin_to_dec(in_bin: list):
    in_bin.reverse()
    res = 0
    for i, x in enumerate(in_bin):
        res += x * (2 ** i)
    return res


class Mode(Enum):
    DEFAULT = 0
    FILE = 1
    RAW = 2
