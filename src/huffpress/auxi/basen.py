"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    BaseN.py

    Contains numeric functionality converting back-forth decimal to a Base N
    number. e.g. binary, hex, base 5, etc.
"""

from typing import List

DEC_RANGE = {int(x): chr(x + 55) for x in range(10, 36)}
DEC_RANGE.update({int(x): str(x) for x in range(0, 10)})
REV_RANGE = {v: k for k, v in DEC_RANGE.items()}


def nmod(x: int, y: int) -> str:
    limit = 36
    if y > limit:
        raise ValueError("limit cannot exceed base 36.")
    if y < 11:
        return str(x % y)
    else:
        return DEC_RANGE[x % y]


def to_basen(num: int, base: int = 2) -> List[str]:
    """
    to_basen(num: int) -> List[str]:

    Convert decimal to binary list

    :param base: base number. for binary, base = 2. for hex, base = 16
    :param num: decimal number
    :return: binary list of 1's 0's
    """
    out_bin = []
    while num > 0:
        out_bin += [nmod(num, base)]
        num //= base
    out_bin.reverse()
    return out_bin


def to_dec(in_bin: List[str], base: int = 2) -> int:
    """
    to_dec(in_bin: List[str]) -> int:

    Convert binary list to decimal integer

    :param base: base number. for binary, base = 2. for hex, base = 16
    :param in_bin: binary list of 1's and 0's
    :return: decimal integer converted from input binary
    """
    in_bin.reverse()
    res = 0
    for i, x in enumerate(in_bin):
        res += REV_RANGE[x] * (base ** i)
    return res
