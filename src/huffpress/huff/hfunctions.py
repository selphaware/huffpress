"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    hfunctions.py

    Contains all Huffman building and deconstructing functions
"""

from collections import Counter
from tqdm import tqdm  # type: ignore
from functools import singledispatch  # type: ignore
from typing import List, Optional, ItemsView
from huffpress.huff.HuffNode import HuffNode
from huffpress.huff.htypes import InputData, TermFreq, Leaves, \
    SortedTree, HuffTuple, HuffCode, HuffTerm, HuffSeq


def calc_term_freq(data: InputData) -> TermFreq:
    """
    calc_term_freq(data: InputData) -> TermFreq:

    Returns dictionary of frequency occurrence counts for each character
    of a given string

    e.g. "ABBcCC" --> { "A": 1, "B": 2, "c": 1, "C": 2 }

    :param data: input string text
    :return: dictionary of character frequency occurrence counts
    """
    count_dat = {
        k if isinstance(k, int) else ord(str(k)): v
        for k, v in dict(Counter(data.data)).items()
    }
    dc: TermFreq = TermFreq(tf=count_dat)
    return dc


def build_leaves(term_freq: TermFreq,
                 verbose: bool = False) -> Leaves:
    """
    build_leaves(term_freq: TermFreq,
                 verbose: bool = False) -> Leaves:

    Builds initial leaf HuffNode's from a given dictionary of character
    frequency occurrence counts

    :param term_freq: dictionary of frequency occurrence counts of a given
    string computed by calc_term_freq function
    :param verbose: set to True for printing console outputs
    :return: dictionary of leaf HuffNode's for a given character frequency
    count dictionary
    """
    if verbose:
        print("Building leaves")
    leaves: Leaves = Leaves(data={
        term: HuffTerm(freq=count, node=HuffNode(term, count))
        for term, count in tqdm(term_freq.tf.items(), disable=not verbose)
    })
    return leaves


def sort_tree(tree: Leaves, verbose: bool = False) -> SortedTree:
    """
    sort_tree(tree: Leaves, verbose: bool = False) -> SortedTree:

    Sorts a Huffman tree dictionary by total frequency ascending order
    returning a list

    e.g.

    { "D": (4, HuffNode), "E": (3, HuffNode),
      "F": (7, HuffNode), "ABC": (2, HuffNode) }

    -->

    [ ("ABC", (2, HuffNode)), ("E", (3, HuffNode)),
      ("D", (4, HuffNode)), ("F", (7, HuffNode)) ]

    :param tree: dictionary of HuffNode's { term : (total-frequency, HuffNode) }
    :param verbose: set to True for printing console outputs
    :return: sorted dictionary of HuffNode's converted to a list
    """
    if verbose:
        print("Sorting tree")
    tree_data: ItemsView[str, HuffTerm] = tree.data.items()
    sorted_leaves: list = sorted(
        tree_data,
        key=lambda pair: pair[1].freq, reverse=False
    )
    term_freq: SortedTree = SortedTree(
        data=[
            HuffSeq(seq_term=x,
                    huff_term=y)
            for x, y in sorted_leaves
        ]
    )
    return term_freq


def build_tree(sorted_new_tree: SortedTree,
               verbose: bool = False) -> Optional[HuffNode]:
    """
    build_tree(sorted_new_tree: SortedTree,
               verbose: bool = False) -> Optional[HuffNode]:

    Builds Huffman tree made out of HuffNode's, constructed from initial
    HuffNode leaves

    :param sorted_new_tree: sorted [ term, (total-frequency, HuffNode) ]
    :param verbose: set to True for printing console outputs
    :return: Built Huffman tree from initial asc sorted  list of leaves
             HuffNode's computed by build_leaves function and sorted by
             sort_tree function
    """
    if verbose:
        print("Building Huffman tree")

    start_len = len(sorted_new_tree.data)
    while_one = start_len == 1  # escape condition for single unique char inputs

    # track progress of tree building
    with tqdm(total=start_len - 1, disable=not verbose) as tbar:

        # traverse through all terms, combining and collapsing least frequent
        # terms into one term (HuffNode).keep on looping through the tree until
        # only one combined term is left. the combined term contains all terms.
        while len(sorted_new_tree.data) > 1 or while_one:

            # build list of (term, total-frequency, HuffNode)
            tree: List[HuffTuple] = [
                HuffTuple(
                    seq_term=huff_seq.seq_term,
                    total_freq=huff_seq.huff_term.freq,
                    node=huff_seq.huff_term.node
                ) for huff_seq in sorted_new_tree.data
            ]

            # check if there is only a single unique character in the input data
            single_char_only = len(tree) <= 1

            # get terms and total-frequencies for first and second tuples
            # first
            first_obj = tree[0]
            first_term = first_obj.seq_term
            first_freq = first_obj.total_freq

            # second
            second_obj = HuffTuple() if single_char_only else tree[1]
            second_term: str = "" if single_char_only else second_obj.seq_term
            second_freq: int = 0 if single_char_only else second_obj.total_freq

            # create new term: combining least two frequent
            # term HuffNode's collapsing into one HuffNode
            new_term = f"{first_term},{second_term}"
            # sum total-frequencies
            new_freq = first_freq + second_freq
            # get HuffNode of first tuple, set to left branch
            new_left = first_obj.node
            # get HuffNode of second tuple, set to right branch
            new_right = None if single_char_only else second_obj.node

            # create new HuffNode, expanding the tree
            node = HuffNode(
                term=new_term,
                freq=new_freq,
                left_child=new_left,
                right_child=new_right
            )

            new_tree: List[HuffTuple]
            # if only single unique char then there is no other chars to process
            if single_char_only:
                new_tree = [HuffTuple(seq_term=new_term,
                                      total_freq=new_freq, node=node)]

            # otherwise: add new term to rest of tree (excluding the first
            # two terms) to be processed.Here we are trimming the list of terms
            # everytime, collapsing the least two frequent terms into one term
            # then continuing to build the tree until only one combined term is
            # left, which is defined in the while loop condition
            else:
                new_tree = tree[2:] + [HuffTuple(seq_term=new_term,
                                                 total_freq=new_freq,
                                                 node=node)]

            # sort tree with least frequent terms at the top
            sorted_new_tree = sort_tree(Leaves(data={
                huff_tuple.seq_term: HuffTerm(freq=huff_tuple.total_freq,
                                              node=huff_tuple.node)
                for huff_tuple in new_tree}))

            # update progress bar
            tbar.update(1)

            # if only single char, we are done, escape.
            if while_one:
                while_one = False

    return sorted_new_tree.data[0].huff_term.node  # returning tree HuffNode object


def print_node(node: Optional[HuffNode], depth: int = 0,
               verbose: bool = True) -> str:
    """
    print_node(node: HuffNode, depth: int = 0, verbose: bool = True) -> str:

    Recursive printing of the HuffNode tree showing all branches, leaves and
    their terms and total-frequencies

    :param node: HuffNode tree i.e. Huffman tree
    :param depth: How many whitespaces to print to represent depth level
                 (starting at depth 0)
    :param verbose: set to True to print to console, False to return string
                    output
    :return: None (prints Huffman tree to console)
    """
    if node is None:
        print("Tree is empty.\n")
        return ""
    else:
        res = ""
        spc = "-" * depth * 2
        line_chr = ("--o" * depth) + (("--" + f"[{depth}> ") * (
            1 if depth else 0))
        if depth == 0:
            dash_chr = ""
            res += "\n"
        else:
            dash_chr = "|"
        res += f"{dash_chr}{line_chr}Term: {node.term}, Freq: {node.freq}\n"
        if node.left_child is not None:
            res += f"|\n{dash_chr}{spc}Left child:\n"
            res += print_node(node.left_child, depth=depth+1, verbose=verbose)
        if node.right_child is not None:
            res += f"|\n{dash_chr}{spc}Right child:\n"
            res += print_node(node.right_child, depth=depth+1, verbose=verbose)
        if verbose:
            print(res)
            return ""
        else:
            return res


@singledispatch
def encode(data, tree: Optional[HuffNode],
           path: str = "", verbose: bool = False):
    """
    encode function calling either:
    encode(int, HuffNode, str); or
    encode(Leaves, HuffNode, bool)
    :param verbose: bool for verbose printing
    :param path: str for 1, 0 paths visited
    :param data: either int (term) or Leaves (initial set of term leaves)
    :param tree: Huffman tree
    """
    raise NotImplementedError(f"Got params {type(data)}, "
                              f"{type(tree)}, {type(path)}, {type(verbose)}")


@encode.register(int)
@encode.register(HuffNode)
@encode.register(str)
def _(single_term: int, tree: Optional[HuffNode], path: str = "") -> HuffCode:
    """
    encode(single_term: int, tree: Optional[HuffNode], path="") -> HuffCode:

    Encode Huffman tree recursively adding 0's to left branches, and 1's to
    right branches.

    Most frequent occurring terms will be encoded with a shorter sequence.
    Least frequent occurring terms will be encoded with a longer sequence

    :param single_term: single character term
    :param tree: HuffNode tree already built by create_huff_tree_encoding function
    :param path: visited nodes collecting 0's (left side), 1's (right side)
                 along the way
    :return: dictionary containing a single term as the key, and its continually
             constructed binary sequence (Huffman map)
    """
    if tree is None:
        return HuffCode(data={})
    elif tree.is_leaf:
        return HuffCode(data={single_term: path})
    else:
        if str(single_term) in str(tree.left_child.term).split(","):
            ret_encode = encode(single_term, tree.left_child, path + "0")
        elif str(single_term) in str(tree.right_child.term).split(","):
            ret_encode = encode(single_term, tree.right_child, path + "1")
        else:
            ret_encode = HuffCode(data={})
        return ret_encode


@encode.register(Leaves)  # type: ignore
@encode.register(HuffNode)
@encode.register(bool)
def _(leaves: Leaves, tree: Optional[HuffNode],
      verbose=False) -> HuffCode:
    """
    encode_all(leaves: Leaves, final_tree: Optional[HuffNode],
               verbose=False) -> HuffCode:

    Encode all unique character terms, constructing binary sequences from the
    Huffman tree

    :param leaves: initial list of leaves with unique character terms
    :param tree: constructed Huffman tree computed by create_huff_tree_encoding
                       function
    :param verbose: set to True to print to console, False to return string
                    output
    :return: dictionary of all terms as keys, and their encoded binary sequence
    """
    if verbose:
        print("Encoding tree")

    terms: List[str] = list(leaves.data.keys())
    res = HuffCode(data={})
    for term in tqdm(terms, disable=not verbose):
        encoded_term = encode(term, tree)
        res.data.update(encoded_term.data)
    return res


@singledispatch
def create_huff_tree(data, verbose: bool = False):
    """
    creates Huffman tree, calling either:
    create_huff_tree(InputData, bool); or
    create_huff_tree(TermFreq, bool)

    :param data: InputData (str or bytes) or TermFreq term frequency counts
    :param verbose: bool - verbose for printing
    """
    raise NotImplementedError(f"Got params {type(data)} and {type(verbose)}")


@create_huff_tree.register(InputData)  # type: ignore
@create_huff_tree.register(bool)
def _(data: InputData, verbose: bool = False):
    """
    create_huff_tree_encoding(data: InputData,
                     verbose: bool = False) -> Tuple[HuffCode,
                                                     Optional[HuffNode]]:

    Method:
        leaves = build_leaves(calc_term_freq(data), verbose=verbose)
        sleaves = sort_tree(leaves)
        huff_tree = build_tree(sleaves, verbose=verbose)
        encod_seq = encode_all(leaves, huff_tree, verbose=verbose)
        return encod_seq, huff_tree

    Main function to create Huffman tree from an input data string

    :param data: input data string or bytearray to be transformed to a
                 Huffman tree
    :param verbose: set to True to print to console, False to return
                    string output
    :return: tuple of final encoded sequences per term and constructed
             Huffman tree
    """
    term_freq: TermFreq = calc_term_freq(data)
    return create_huff_tree(term_freq, verbose=verbose)


@create_huff_tree.register(TermFreq)  # type: ignore
@create_huff_tree.register(bool)
def _(data: TermFreq, verbose: bool = False):
    """

    :param data:
    :param verbose:
    :return:
    """
    leaves: Leaves = build_leaves(data, verbose=verbose)
    sleaves: SortedTree = sort_tree(leaves)
    huff_tree: Optional[HuffNode] = build_tree(sleaves, verbose=verbose)
    encod_seq: HuffCode = encode(leaves, tree=huff_tree, verbose=verbose)
    return encod_seq, huff_tree
