"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    htypes.py

    Contains all Huffman Data Structure Types
"""

from dataclasses import dataclass
from typing import Union, Dict, List, Optional
from huffpress.huff.HuffNode import HuffNode


@dataclass
class InputData:
    """
    data = Union[str, bytes]

    Input data to be compressed will either be a string or sequence of bytes
    string e.g. "Hello"
    bytes e.g. b"ABC" or [65, 66, 67]
    """
    data: Union[str, bytes]


@dataclass
class CompData:
    """
    data = Union[str, bytearray]

    Data to be compressed will either be the filename (str) or compressed data
    (bytearray)
    """
    data: Union[str, bytearray]


@dataclass
class TermFreq:
    """
    tf = Dict[str, int]

    When calculating collections.Counter on a input string or bytes,
    we return a dictionary of key being the ordinal ASCII value, and
    the value being the frequency of occurrence in the input data.
    """
    tf: Dict[int, int]


@dataclass
class HuffTerm:
    """
    freq = int
    node = Optional[HuffNode]]

    For a single Huffman Node we have a total number of frequency
    occurrences, and we have the node (which can be null)
    """
    freq: int
    node: Optional[HuffNode]


@dataclass
class Leaves:
    """
    data = Dict[str, HuffTerm]

    Initial set of leaves set as a dictionary of keys as the term made up of
    comma delimited ordinal ASCII values, and the value as the HuffTerm.
    """
    data: Dict[str, HuffTerm]


@dataclass
class HuffSeq:
    """
    seq_term = str
    huff_term = HuffTerm

    Huffman sequence made up of the sequence of terms string and the HuffTerm
    """
    seq_term: str
    huff_term: HuffTerm


@dataclass
class SortedTree:
    """
    data = List[Tuple[str, HuffTerm]]

    Huffman tree structure, which is a list of tuples of the term made up of
    comma delimited ordinal ASCII values, and the HuffTerm. The list is sorted
    by the total number of frequency order in ascending order.
    """
    data: List[HuffSeq]


@dataclass
class HuffTuple:
    """
    seq_term = str
    total_freq = int,
    node = Optional[HuffNode]

    Similar structure to SortedTree where we have string term,
    total frequency, and the HuffNode (which could be null)
    """
    seq_term: str = ""
    total_freq: int = -1
    node: Optional[HuffNode] = None


@dataclass
class HuffCode:
    """
    HuffCode = Dict[int, str]

    Final encoded Huffman encoded sequences with key as the ordinal ASCII value
    and the value as the binary sequence string
    """
    data: Dict[int, str]
