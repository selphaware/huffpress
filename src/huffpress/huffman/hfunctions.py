"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    hfunctions.py

    Contains all Huffman building and deconstructing functions
"""

from collections import Counter
from tqdm import tqdm
from huffpress.huffman.HuffNode import HuffNode


def calc_term_freq(data: str) -> dict:
    """
    calc_term_freq(data: str) -> dict:

    Returns dictionary of frequency occurrence counts for each character of a given string

    e.g. "ABBcCC" --> { "A": 1, "B": 2, "c": 1, "C": 2 }

    :param data: input string text
    :return: dictionary of character frequency occurrence counts
    """
    dc = Counter(data)
    return dict(dc)


def build_leaves(term_freq: dict, verbose: bool = False) -> dict:
    """
    build_leaves(term_freq: dict, verbose=False) -> dict:

    Builds initial leaf HuffNode's from a given dictionary of character frequency occurrence counts

    :param term_freq: dictionary of frequency occurrence counts of a given string computed by calc_term_freq function
    :param verbose: set to True for printing console outputs
    :return: dictionary of leaf HuffNode's for a given character frequency count dictionary
    """
    if verbose:
        print("Building leaves")
    return {k: (v, HuffNode(k, v)) for k, v in tqdm(term_freq.items(), disable=not verbose)}


def sort_tree(tree: dict, verbose: bool = False) -> list:
    """
    sort_tree(tree: dict) -> list:

    Sorts a Huffman tree dictionary by total frequency ascending order returning a list

    e.g.

    { "D": (4, HuffNode), "E": (3, HuffNode), "F": (7, HuffNode), "ABC": (2, HuffNode) }

    -->

    [ ("ABC", (2, HuffNode)), ("E": (3, HuffNode)), ("D": (4, HuffNode)), ("F": (7, HuffNode)) ]

    :param tree: dictionary of HuffNode's { term : (total-frequency, HuffNode) }
    :param verbose: set to True for printing console outputs
    :return: sorted dictionary of HuffNode's converted to a list
    """
    if verbose:
        print("Sorting tree")
    term_freq = sorted(tree.items(), key=lambda pair: pair[1][0], reverse=False)
    return term_freq


def build_tree(sorted_new_tree: list, verbose: bool = False) -> HuffNode:
    """
    build_tree(leaves: list, verbose=False) -> list:

    Builds Huffman tree made out of HuffNode's, constructed from initial HuffNode leaves

    :param sorted_new_tree: sorted [ term, (total-frequency, HuffNode) ]
    :param verbose: set to True for printing console outputs
    :return: Built Huffman tree from initial asc sorted  list of leaves HuffNode's
            computed by build_leaves function and sorted by sort_tree function
    """
    if verbose:
        print("Building Huffman tree")

    start_len = len(sorted_new_tree)
    while_one = start_len == 1  # escape condition for single unique character inputs

    # track progress of tree building
    with tqdm(total=start_len - 1, disable=not verbose) as tbar:

        # traverse through all terms, combining and collapsing least frequent terms into one term (HuffNode).
        # keep on looping through the tree until only one combined term is left. the combined term contains
        # all terms.
        while len(sorted_new_tree) > 1 or while_one:

            # build list of (term, total-frequency, HuffNode)
            tree = [(x, y, z) for x, (y, z) in sorted_new_tree]

            # check if there is only a single unique character in the input data
            single_char_only = len(tree) <= 1

            # get terms and total-frequencies for first and second tuples
            # first
            first_obj = tree[0]
            first_term = first_obj[0]
            first_freq = first_obj[1]

            # second
            second_obj = None if single_char_only else tree[1]
            second_term = "" if single_char_only else f",{second_obj[0]}"
            second_freq = 0 if single_char_only else second_obj[1]

            # create new term: combining least two frequent term HuffNode's collapsing into one HuffNode
            new_term = f"{first_term}{second_term}"
            new_freq = first_freq + second_freq  # sum total-frequencies
            new_left = first_obj[2]  # get HuffNode of first tuple, set to left branch
            new_right = None if single_char_only else second_obj[2]  # get HuffNode of second tuple, set to right branch

            # create new HuffNode, expanding the tree
            node = HuffNode(
                term=new_term,
                freq=new_freq,
                left_child=new_left,
                right_child=new_right
            )

            # if only single unique char then there is no other chars to process
            if single_char_only:
                new_tree = [(new_term, new_freq, node)]

            # otherwise: add new term to rest of tree (excluding the first two terms) to be processed.
            # Here we are trimming the list of terms everytime, collapsing the least two frequent terms
            # into one term then continuing to build the tree until only one combined term is left, which is
            # defined in the while loop condition
            else:
                new_tree = tree[2:] + [(new_term, new_freq, node)]

            # sort tree with least frequent terms at the top
            sorted_new_tree = sort_tree({k: (f, n) for k, f, n in new_tree})

            # update progress bar
            tbar.update(1)

            # if only single char, we are done, escape.
            if while_one:
                while_one = False

    return sorted_new_tree[0][1][1]  # returning tree HuffNode object


def print_node(node: HuffNode, depth: int = 0, verbose: bool = True) -> str:
    """
    print_node(node: HuffNode) -> None:

    Recursive printing of the HuffNode tree showing all branches, leaves and their terms and total-frequencies

    :param node: HuffNode tree i.e. Huffman tree
    :param depth: How many whitespaces to print to represent depth level (starting at depth 0)
    :param verbose: set to True to print to console, False to return string output
    :return: None (prints Huffman tree to console)
    """
    res = ""
    spc = "-" * depth * 2
    line_chr = ("--o" * depth) + (("--" + f"[{depth}> ") * (1 if depth else 0))
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


def encode(term, tree: HuffNode, path=""):
    if tree is None:
        return ""
    elif tree.is_leaf:
        return {term: path}
    else:
        if str(term) in str(tree.left_child.term).split(","):
            return encode(term, tree.left_child, path + "0")
        elif str(term) in str(tree.right_child.term).split(","):
            return encode(term, tree.right_child, path + "1")


def encode_all(leaves: dict, final_tree: HuffNode, verbose=False):
    if verbose:
        print("Encoding tree")

    terms = leaves.keys()
    res = {}
    for term in tqdm(terms, disable=not verbose):
        res.update(encode(term, final_tree))
    return res


def create_huff_tree(data: str, verbose: bool = False):
    leaves = build_leaves(calc_term_freq(data), verbose=verbose)
    sleaves = sort_tree(leaves)
    mtree = build_tree(sleaves, verbose=verbose)
    f_tree = encode_all(leaves, mtree, verbose=verbose)
    return f_tree, mtree
