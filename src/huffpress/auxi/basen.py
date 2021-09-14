"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    BaseN.py

    Contains numeric functionality converting back-forth decimal to a Base N
    number. e.g. binary, hex, base 5, etc.
"""

from typing import List
from huffpress.auxi.imdict import ImDict
from functools import singledispatch


class BaseRange:
    """
    BaseRange class holding the following static consts:

    -- dec: dict --
    decimal to base range i.e. {10: A, 11:B, ..., 35: Z} and rest of the
    decimal to base range {1: 1, 2:2, ..., 9:9, 10:A, ..., 35: Z}

    -- rev: dict --

    """
    dec: ImDict = ImDict({
        **{int(x): chr(x + 55) for x in range(10, 36)},
        **{int(x): str(x) for x in range(0, 10)}
    })

    rev: ImDict = ImDict({v: k for k, v in dec.items()})


def nmod(x: int, y: int) -> str:
    """
    BaseN modulo operator

    nmod(10, 16) = "A"
    nmod(10, 2) = "0"

    :param x: number
    :param y: modulo
    :return: remainder
    """
    limit = 36
    if y > limit:
        raise ValueError("modulo y cannot exceed base 36.")
    else:
        return BaseRange.dec[x % y]


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
        res += BaseRange.rev[x] * (base ** i)
    return res


@singledispatch
def basen(in_num, fbase: int = 10, tbase: int = 2):
    """
    converts number in_num from base fbase to base tbase
    see overloads below

    :param in_num: number to convert: either str or List[str]
    :param fbase: from base
    :param tbase: to base
    :return: List[str] value conversion
    """
    if not(isinstance(in_num, list) or isinstance(in_num, str)):
        raise TypeError("in_num must be either List[str] or str"
                        f"Types: {type(in_num)}, {type(fbase)}, {type(tbase)}")


@basen.register(list)
@basen.register(int)
@basen.register(int)
def _(in_num: List[str], fbase: int = 10, tbase: int = 2) -> List[str]:
    """
    Convert number in_num from Base of fbase to Base of tbase.

    :param in_num: list of numbers e.g. ["16", "F"] is a hex number 16F
    :param fbase: from base conversion
    :param tbase: to base conversion
    :return: resulting List[str] value converting in_num from fbase to tbase
    """
    val: List[str]
    if fbase == 10:
        val = to_basen(int("".join(in_num)), tbase)
    else:
        dec_n = to_dec(in_num, fbase)
        val = to_basen(dec_n, tbase)
    return val


@basen.register(str)  # type: ignore
@basen.register(int)
@basen.register(int)
def _(in_num: str, fbase: int = 10, tbase: int = 2) -> List[str]:
    """
    Convert number in_num from Base of fbase to Base of tbase.

    :param in_num: list of numbers e.g. ["16", "F"] is a hex number 16F
    :param fbase: from base conversion
    :param tbase: to base conversion
    :return: resulting List[str] value converting in_num from fbase to tbase
    """
    return basen(list(in_num), fbase, tbase)
