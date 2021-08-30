from collections import Counter
from tqdm import tqdm


class HuffNode(object):
    def __init__(self, term: str, freq: int, left_child=None, right_child=None):
        self.term = term
        self.freq = freq
        self.left_child = left_child
        self.right_child = right_child

    @property
    def is_leaf(self):
        return (self.left_child is None) and (self.right_child is None)


def calc_term_freq(data):
    dc = Counter(data)
    return dict(dc)


def build_leaves(term_freq: dict) -> dict:
    return {k: (v, HuffNode(k, v)) for k, v in tqdm(term_freq.items())}


def sort_tree(tree: dict):
    term_freq = sorted(tree.items(), key=lambda pair: pair[1][0], reverse=False)
    return term_freq


def build_tree(leaves: list):
    start_len = len(leaves)
    with tqdm(total=start_len - 1) as tbar:
        while len(leaves) > 1:
            ls = [(x, y, z) for x, (y, z) in leaves]
            new_term = f"{ls[0][0]},{ls[1][0]}"
            new_freq = ls[0][1] + ls[1][1]
            new_left = ls[0][2]
            new_right = ls[1][2]
            node = HuffNode(
                term=new_term,
                freq=new_freq,
                left_child=new_left,
                right_child=new_right
            )
            new_ls = ls[2:] + [(new_term, new_freq, node)]
            leaves = sort_tree({k: (f, n) for k, f, n in new_ls})
            tbar.update(1)
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


def encode_all(leaves: dict, final_tree: HuffNode):
    terms = leaves.keys()
    res = {}
    for term in tqdm(terms):
        res.update(encode(term, final_tree))
    return res


def create_huff_tree(data):
    print("building leaves")
    leaves = build_leaves(calc_term_freq(data))
    print("sorting tree")
    sleaves = sort_tree(leaves)
    print("building tree")
    new_t = build_tree(sleaves)
    mtree = new_t[0][1][1]
    print("encoding tree")
    f_tree = encode_all(leaves, mtree)
    return f_tree, mtree


def create_huff_sequence(huff: dict, itxt):
    new_str = ""
    for i in tqdm(itxt):
        new_str += huff[i]
    rem = 8 - (len(new_str) % 8)
    new_str += "0" * rem
    return rem, new_str


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


def create_final_sequence(huff_seq: tuple):
    bin_rem = "".join(list(map(str, dec_to_bin(huff_seq[0]))))
    bin_rem = bin_rem.rjust(8, "0")
    data = bin_rem + huff_seq[1]
    return data


def create_seq_bins(final_seq: str):
    res = []
    fin = len(final_seq) // 8
    for i in tqdm(range(fin)):
        start = (i * 8)
        end = (i + 1) * 8
        res.append(final_seq[start:end])
    return res


def create_seq_chars(final_bins):
    res = []
    for fbin in tqdm(final_bins):
        val = bin_to_dec(list(map(int, list(fbin))))
        # final_val = chr(val)
        res.append(val)
    return bytearray(res)


def reverse_final_sequence(bstr):
    data = list(bstr)
    rem = data[0]
    data = data[1:]
    fbin = ""
    for dec in tqdm(data):
        dbin = dec_to_bin(dec)
        vbin = "".join(list(map(str, dbin))).rjust(8,"0")
        fbin += vbin
    fbin = fbin[:-rem]
    return fbin


def reverse_huff_sequence(huff: dict, seq: str):
    term = ""
    res = []
    huff = {v: k for k, v in huff.items()}
    for sq in tqdm(seq):
        term += sq
        val = huff.get(term)
        if val is not None:
            res.append(val)
            term = ""
    return bytearray(res)
