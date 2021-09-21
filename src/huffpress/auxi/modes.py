"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    modes.py

    Contains all modes used in the rest of the codebase (currently we only
    have 1 mode).
"""

from enum import Enum


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
