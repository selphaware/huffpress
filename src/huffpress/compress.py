"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    compress.py

    Contains all compression functions using the Huffman encoding algorithm to
    encode most frequently occurring terms with short binary sequences,
    and encoding least frequently occurring terms with longer binary sequences.

    Process:
    -------
    1) Input String -> 2) ASCII ordinal values -> 3) Huffman Encoding
    -> 4) Replace characters with Encodings -> NOTE: Most frequent characters
    will have shorter encodings than Least frequent characters. The idea is
    there will be numerous frequent characters, which can be replaced by a short
    binary encoding - and so when we 5) Pack binaries into buckets of
    length 8 -> we combine 2 or more characters into a single 8-bit byte,
    and hence 6) Convert the binaries of length 8 to decimal and 7) The decimals
    are ASCII ordinal values which can be converted to characters
    (ASCII values between 1 and 255).
"""

import json
import os
# noinspection Mypy
from tqdm import tqdm
from typing import Union, Tuple, List, Optional
from huffpress.generic import bin_to_dec, dec_to_bin, Mode
from huffpress.huffman.hfunctions import create_huff_tree
from huffpress.huffman.htypes import InputData, HuffCode
from huffpress.huffman.HuffNode import HuffNode


def create_huff_sequence(huff: HuffCode, inp_data: InputData,
                         verbose: bool = False) -> Tuple[int, str]:
    """
    create_huff_sequence(huff: dict, inp_data: Union[str, bytearray],
                         verbose: bool = False) -> tuple:

    Creates an encoded Huffman sequence from a given Huffman tree dictionary
    and input data string text.

    :param huff: Huffman tree dictionary (encoded sequences per term)
                computed by hfunctions.create_huff_tree
    :param inp_data: input data string text to be encoded
    :param verbose: set to True for printing console outputs
    :return: (number of 0 paddings required, new encoded sequence)
    """
    new_str = ""
    for i in tqdm(inp_data, disable=not verbose):
        new_str += huff[i]
    rem = 8 - (len(new_str) % 8)
    new_str += "0" * rem
    return rem, new_str


def create_final_sequence(huff_seq_rem: Tuple[int, str],
                          verbose: bool = False) -> str:
    """
    create_final_sequence(huff_seq: tuple, verbose=False) -> str:

    From a given Huffman encoded sequence (computed by create_huff_sequence
    function), convert to a binary sequence.

    :param huff_seq_rem: tuple of 0:Huffman sequence and 1:remainder length
                        (to be used for '0' padding)
    :param verbose: set to True for printing console outputs
    :return: final Huffman sequence converted to a binary sequence
    """
    if verbose:
        print("Generating final sequence")
    bin_rem = "".join(list(map(str, dec_to_bin(huff_seq_rem[0]))))
    bin_rem = bin_rem.rjust(8, "0")
    data = bin_rem + huff_seq_rem[1]
    return data


def create_seq_bins(final_seq: str, verbose: bool = False) -> List[str]:
    """
    create_seq_bins(final_seq: str, verbose: bool = False) -> list:

    From a given final Huffman sequence (computed by create_final_sequence
    function) extract the sequence of binaries of length 8 and store in a list

    :param final_seq: Final Huffman sequence string of binaries
    :param verbose: set to True for printing console outputs
    :return:
    """
    res = []
    fin = len(final_seq) // 8
    for i in tqdm(range(fin), disable=not verbose):
        start = (i * 8)
        end = (i + 1) * 8
        res.append(final_seq[start:end])
    return res


def compress_seq_bins(final_bins: List[str],
                      verbose: bool = False) -> bytearray:
    """
    compress_seq_bins(final_bins: list, verbose: bool = False) -> bytearray:

    From a given list of binaries constructed from the final Huffman sequence
    i.e. create_seq_bins function, compress the binaries (converting) to an
    ASCII ordinal value.

    :param final_bins: list of binary sequences construct from the final
                        Huffman sequence
    :param verbose: set to True for printing console outputs
    :return: bytearray of ascii ordinal values constructed from the Huffman
            sequence of binaries, which collapses 2 or
            more characters into less number of characters for most frequent
            occurring terms in the original raw data
    """
    res = []
    for fbin in tqdm(final_bins, disable=not verbose):
        val = bin_to_dec(list(map(int, list(fbin))))
        res.append(val)
    return bytearray(res)


def add_huff_map(final_seq: bytearray, huff_map: HuffCode) -> bytearray:
    """
    add_huff_map(final_seq: bytearray, huff_map: dict) -> bytearray

    Concatenate the final generated Huffman sequence with the Huffman map,
    which is required for decoding the Huffman sequence.

    :param final_seq: final compressed Huffman sequence binaries computed by
                    compress_seq_bins function
    :param huff_map: Huffman map containing terms and their encoding
    :return: concatenated final_seq + huff_map in a bytearray sequence
    """
    huff_bytes = [ord(x) for x in list(json.dumps(huff_map)
                                       .replace(chr(32), ""))]
    huff_array = bytearray(huff_bytes)
    huff_len = list(map(lambda x: ord(str(x)), dec_to_bin(len(huff_array))))
    final_res = final_seq + huff_array + bytearray(huff_len)
    return final_res


def compress_bytes(inp_bytes: bytes, verbose: bool = False) -> bytearray:
    """
    compress_bytes(inp_bytes: bytes, verbose: bool = False) -> bytearray:

    Compress input data bytes using the Huffman Encoding algorithm.
    Function compress_string takes an input string which transforms to bytes,
    then calls this function to compress.

    :param inp_bytes: input data bytes to be compressed
    :param verbose: set to True for printing console outputs
    :return: Final compressed bytearray sequence
    """
    encod_seq: HuffCode
    huff_tree: Optional[HuffNode]
    encod_seq, huff_tree = create_huff_tree(inp_bytes, verbose=verbose)
    huff_seq: Tuple[int, str] = create_huff_sequence(encod_seq, inp_bytes,
                                                     verbose=verbose)
    final_seq: str = create_final_sequence(huff_seq, verbose=verbose)
    seq_bins: List[str] = create_seq_bins(final_seq, verbose=verbose)
    final_res: bytearray = compress_seq_bins(seq_bins, verbose=verbose)
    app_res = add_huff_map(final_res, encod_seq)

    return app_res


def compress_string(inp_st: str, verbose: bool = False) -> bytearray:
    """
    compress_string(inp_st: str, verbose=False) -> bytearray:

    Compresses input string using the Huffman Encoding algorithm

    :param inp_st: input string to be compressed
    :param verbose: set to True for printing console outputs
    :return: compressed data in bytearray format
    """
    inp_bytes = bytearray([ord(x) for x in list(inp_st)])
    return compress_bytes(inp_bytes, verbose=verbose)


def compress_file(inp_file: str, verbose: bool = False):
    """
    compress_file(inp_file: str, verbose: bool = False):

    Compresses the contents of a file and outputs to a file
    with extension ".hac"

    e.g. some_file.ext --- compressed to --> some_file.ext.hac

    :param inp_file: input file to compress
    :param verbose: set to True for printing console outputs
    :return: name of the compressed output file
    """
    with open(inp_file, "rb") as f:
        inp_str: bytes = f.read()
    comp_str = compress_bytes(inp_str, verbose=verbose)
    outfile = f"{inp_file}.hac"
    with open(outfile, "wb") as f:
        f.write(comp_str)
    return outfile


def compress(inp: str, verbose: bool = False,
             mode: Mode = Mode.DEFAULT) -> Union[bytearray, str]:
    """
    compress(inp: str, verbose: bool = False,
             mode: Mode = Mode.DEFAULT) -> Union[bytearray, str]:

    Generic compression function taking in input either filename or
    string to compress.

    :param inp: filename or string text to compress
    :param verbose: set to True for printing console outputs
    :param mode:
                Mode.DEFAULT --> if file exists, compress file, otherwise
                                 compress string text
                Mode.FILE    --> compress file
                Mode.RAW     --> compress string text
    :return: if compressed file, return compressed output filename. otherwise,
             return bytearray compressed data
    """
    if not isinstance(inp, str):
        raise TypeError("input must be a string: either a filename "
                        "including path OR a text.")
    else:
        if (mode is not Mode.RAW) and os.path.exists(inp):
            return compress_file(inp, verbose=verbose)
        else:
            return compress_string(inp, verbose=verbose)
