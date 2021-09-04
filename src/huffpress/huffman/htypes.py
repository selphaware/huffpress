"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    htypes.py

    Contains all Huffman Data Structure Types:

    ----------------

    InputData = Union[str, bytes]

    Input data will either be a string or sequence of bytes
    string e.g. "Hello"
    bytes e.g. b"ABC" or [65, 66, 67]

    ----------------

    TermFreq = Dict[str, int]

    When calculating collections.Counter on a input string or bytes,
    we return a dictionary of key being the ordinal ASCII value, and
    the value being the frequency of occurrence in the input data.

    ----------------

    HuffTerm = Tuple[int, Optional[HuffNode]]

    For a single Huffman Node we have a tuple of total number of frequency
    occurrences, and we have the node (which can be null)

    ----------------

    Leaves = Dict[str, HuffTerm]

    Initial set of leaves set as a dictionary of keys as the term made up of
    comma delimited ordinal ASCII values, and the value as the HuffTerm.

    ----------------

    SortedTree = List[Tuple[str, HuffTerm]]

    Huffman tree structure, which is a list of tuples of the term made up of
    comma delimited ordinal ASCII values, and the HuffTerm. The list is sorted
    by the total number of frequency order in ascending order.

    ----------------

    HuffTuple = Tuple[str, int, Optional[HuffNode]]

    Similar structure to SortedTree where we have a tuple of string term,
    total frequency, and the HuffNode (which could be null)

    ----------------

    HuffCode = Dict[int, str]

    Final encoded Huffman encoded sequences with key as the ordinal ASCII value
    and the value as the binary sequence string
"""

from typing import Union, Dict, Tuple, List, Optional
from huffpress.huffman.HuffNode import HuffNode

InputData = Union[str, bytes]
TermFreq = Dict[int, int]
HuffTerm = Tuple[int, Optional[HuffNode]]
Leaves = Dict[str, HuffTerm]
SortedTree = List[Tuple[str, HuffTerm]]
HuffTuple = Tuple[str, int, Optional[HuffNode]]
HuffCode = Dict[int, str]
