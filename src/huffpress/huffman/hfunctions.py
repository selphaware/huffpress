from collections import Counter

from tqdm import tqdm

from huffpress.huffman.HuffNode import HuffNode


def sort_tree(tree: dict):
    term_freq = sorted(tree.items(), key=lambda pair: pair[1][0], reverse=False)
    return term_freq


def calc_term_freq(data):
    dc = Counter(data)
    return dict(dc)


def build_leaves(term_freq: dict, verbose=False):
    return {k: (v, HuffNode(k, v)) for k, v in tqdm(term_freq.items(), disable=not verbose)}


def build_tree(leaves: list, verbose=False):
    start_len = len(leaves)
    while_one = start_len == 1
    with tqdm(total=start_len - 1, disable=not verbose) as tbar:
        while len(leaves) > 1 or while_one:
            ls = [(x, y, z) for x, (y, z) in leaves]
            fterm = ls[0][0]
            sterm = "" if len(ls) <= 1 else f",{ls[1][0]}"
            new_term = f"{fterm}{sterm}"
            ffreq = ls[0][1]
            sfreq = 0 if len(ls) <= 1 else ls[1][1]
            new_freq = ffreq + sfreq
            new_left = ls[0][2]
            new_right = None if len(ls) <= 1 else ls[1][2]
            node = HuffNode(
                term=new_term,
                freq=new_freq,
                left_child=new_left,
                right_child=new_right
            )
            if len(ls) <= 1:
                new_ls = [(new_term, new_freq, node)]
            else:
                new_ls = ls[2:] + [(new_term, new_freq, node)]
            leaves = sort_tree({k: (f, n) for k, f, n in new_ls})
            tbar.update(1)
            if while_one:
                while_one = False
    return leaves


def print_node(node: HuffNode):
    print(f"Term: {node.term}, Freq: {node.freq}")
    if node.left_child is not None:
        print("\nLeft child:")
        print_node(node.left_child)
    if node.right_child is not None:
        print("\nRight child:")
        print_node(node.right_child)


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
    terms = leaves.keys()
    res = {}
    for term in tqdm(terms, disable=not verbose):
        res.update(encode(term, final_tree))
    return res


def create_huff_tree(data, verbose=False):
    if verbose:
        print("Building leaves")
    leaves = build_leaves(calc_term_freq(data), verbose=verbose)
    if verbose:
        print("Sorting tree")
    sleaves = sort_tree(leaves)
    if verbose:
        print("Building Huffman tree")
    new_t = build_tree(sleaves, verbose=verbose)
    mtree = new_t[0][1][1]
    if verbose:
        print("Encoding tree")
    f_tree = encode_all(leaves, mtree, verbose=verbose)
    return f_tree, mtree
