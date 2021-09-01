"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    compress.py

    Contains all compression functions using the Huffman encoding algorithm to
    encode most frequently occurring terms with short binary sequences,
    and encoding least frequently occurring terms with longer binary sequences.
"""

import json
import os
from tqdm import tqdm
from huffpress.generic import bin_to_dec, dec_to_bin, Mode
from huffpress.huffman.hfunctions import create_huff_tree


def create_huff_sequence(huff: dict, itxt: str, verbose: bool = False) -> tuple:
    """
    create_huff_sequence(huff: dict, itxt: str, verbose: bool = False) -> tuple:

    Creates an encoded Huffman sequence from a given Huffman tree dictionary and input data string text.

    :param huff: Huffman tree dictionary (encoded sequences per term) computed by hfunctions.create_huff_tree
    :param itxt: input data string text to be encoded
    :param verbose: set to True for printing console outputs
    :return: (number of 0 paddings required, new encoded sequence)
    """
    new_str = ""
    for i in tqdm(itxt, disable=not verbose):
        new_str += huff[i]
    rem = 8 - (len(new_str) % 8)
    new_str += "0" * rem
    return rem, new_str


def create_final_sequence(huff_seq: tuple, verbose=False):
    """

    :param huff_seq:
    :param verbose:
    :return:
    """
    if verbose:
        print("Generating final sequence")
    bin_rem = "".join(list(map(str, dec_to_bin(huff_seq[0]))))
    bin_rem = bin_rem.rjust(8, "0")
    data = bin_rem + huff_seq[1]
    return data


def create_seq_bins(final_seq: str, verbose=False):
    res = []
    fin = len(final_seq) // 8
    for i in tqdm(range(fin), disable=not verbose):
        start = (i * 8)
        end = (i + 1) * 8
        res.append(final_seq[start:end])
    return res


def create_seq_chars(final_bins, verbose=False):
    res = []
    for fbin in tqdm(final_bins, disable=not verbose):
        val = bin_to_dec(list(map(int, list(fbin))))
        # final_val = chr(val)
        res.append(val)
    return bytearray(res)


def add_huff_map(final_seq, huff_map: dict):
    huff_bytes = [ord(x) for x in list(json.dumps(huff_map).replace(chr(32), ""))]
    huff_array = bytearray(huff_bytes)
    huff_len = list(map(lambda x: ord(str(x)), dec_to_bin(len(huff_array))))
    final_res = final_seq + huff_array + bytearray(huff_len)
    return final_res


def compress_bytes(inp_st, verbose=False):
    encod_seq, huff_tree = create_huff_tree(inp_st, verbose=verbose)
    huff_seq = create_huff_sequence(encod_seq, inp_st, verbose=verbose)
    final_seq = create_final_sequence(huff_seq, verbose=verbose)
    seq_bins = create_seq_bins(final_seq, verbose=verbose)
    final_res = create_seq_chars(seq_bins, verbose=verbose)
    app_res = add_huff_map(final_res, encod_seq)

    return app_res


def compress_string(inp_st: str, verbose=False):
    inp_bytes = bytearray([ord(x) for x in list(inp_st)])
    return compress_bytes(inp_bytes, verbose=verbose)


def compress_file(inp_file: str, verbose=False):
    with open(inp_file, "rb") as f:
        inp_str = f.read()
    comp_str = compress_bytes(inp_str, verbose=verbose)
    outfile = f"{inp_file}.hac"
    with open(outfile, "wb") as f:
        f.write(comp_str)
    return outfile


def compress(inp, verbose=False, mode=Mode.DEFAULT):
    if not isinstance(inp, str):
        raise TypeError("input must be a string: either a filename including path OR a text.")
    else:
        if (mode is not Mode.RAW) and os.path.exists(inp):
            return compress_file(inp, verbose=verbose)
        else:
            return compress_string(inp, verbose=verbose)
