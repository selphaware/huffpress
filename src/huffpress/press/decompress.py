"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    decompress.py

    Contains all decompression functions by first extracting the Huffman map
    from the input data and using the map to convert back the compressed
    characters to the original characters.
"""
import json
from tqdm import tqdm  # type: ignore
from typing import Tuple, Optional
from huffpress.auxi.basen import to_basen, to_dec, basen
from huffpress.huff.htypes import HuffCode, CompData


def reverse_final_sequence(bstr: bytes, verbose: bool = False) -> str:
    """
    reverse_final_sequence(bstr: bytearray, verbose: bool = False) -> str:

    Convert the input (already compressed sequence) of ascii ordinal values to
    a binary sequence string, which is the encoded Huffman sequence

    :param bstr: input sequence of ascii ordinal values (compressed data
                 bytearray format)
    :param verbose: set to True for printing console outputs
    :return: binary string of compressed data (Huffman encoded sequence
             of 0's and 1's)
    """
    if verbose:
        print("Reversing final sequence")
    data = list(bstr)
    rem = data[0]
    data = data[1:]
    fbin = ""
    for dec in tqdm(data, disable=not verbose):
        dbin = to_basen(dec)
        vbin = "".join(list(map(str, dbin))).rjust(8, "0")
        fbin += vbin
    fbin = fbin[:-rem]
    return fbin


def reverse_huff_sequence(huff_map: HuffCode, seq: str,
                          verbose: bool = False) -> bytearray:
    """
    reverse_huff_sequence(huff: HuffCode, seq: str,
                          verbose: bool = False) -> bytearray:

    Reverse the input binary string Huffman encoded sequence --> back to the
    original characters. This is done by traversing through the sequence in
    order and identifying any of the Huffman encoded sequence from the
    given (huff) Huffman map. Since all encodings are unique at any length,
    we can replace in this forward travelling manner.

    :param huff_map: Huffman map containing the binary encodings to original
                 character
    :param seq: input binary string of Huffman encoded sequence
    :param verbose: set to True for printing console outputs
    :return:
    """
    if verbose:
        print("Reversing Huffman sequence")
    term = ""
    res = []
    huff_trn = {v: k for k, v in huff_map.data.items()}
    for sq in tqdm(seq, disable=not verbose):
        term += sq
        val = huff_trn.get(term)  # TODO: Huff-Squared here
        if val is not None:
            res.append(val)
            term = ""
    return bytearray(res)


def extract_huff_map(inp_bytes: bytes,
                     verbose: bool = False) -> Tuple[HuffCode, int]:
    """
    extract_huff_map(inp_bytes: bytes,
                     verbose: bool = False) -> Tuple[HuffCode, int]:

    Extract Huffman encoding dictionary map from the input data.

    :param inp_bytes: input sequence of bytes containing compressed data
                      and Huffman map
    :param verbose: set to True for printing console outputs
    :return: Huffmann map dictionary and the length of the map
    """
    if verbose:
        print("Extracting Huffman Tree")
    rev_str = list(inp_bytes)
    rev_str.reverse()
    rev_bytes = bytearray(rev_str)
    huff_len_bytes = []
    for r in rev_bytes:
        if r == ord('}'):
            break
        huff_len_bytes.append(r)
    huff_len_bytes.reverse()
    huff_len = to_dec(list(map(lambda x: chr(x), huff_len_bytes)))
    len_of_len = len(huff_len_bytes)
    huff_dic_str = inp_bytes[-(huff_len + len_of_len): -len_of_len]
    huff_map = {int(k): v
                for k, v in json.loads(bytearray(huff_dic_str)).items()}

    # convert huff_map values from radix-36 to binary (base-2)
    # and remove leading "1", which was added to handle encoded
    # sequences starting with 0. e.g. 4 --> 100 --> 00
    huff_map = {k: basen(v, 36, 2, True)[1:] for k, v in huff_map.items()}

    return HuffCode(data=huff_map), len_of_len + len(huff_dic_str)


def decompress_bytes(inp_bytes: bytes, verbose=False) -> bytearray:
    """
    decompress_bytes(inp_bytes: bytes, verbose=False) -> bytearray:

    Main function to decompress input bytes by extracting the Huffman map
    and using the map to replace the encoded sequences with the original
    characters.

    :param inp_bytes: Input data to be compressed
    :param verbose: set to True for printing console outputs
    :return: decompressed bytearray data
    """
    huff_map: HuffCode
    rem: int
    huff_map, rem = extract_huff_map(inp_bytes, verbose=verbose)
    inp_bytes = inp_bytes[:-rem]
    rev_seq: str = reverse_final_sequence(inp_bytes, verbose=verbose)
    res: bytearray = reverse_huff_sequence(huff_map, rev_seq, verbose=verbose)
    return res


def decompress_file(inp_file: str, outfile: Optional[str] = None,
                    verbose=False):
    """
    decompress_file(inp_file: str, outfile: Optional[str] = None,
                    verbose=False):

    Decompress file

    :param inp_file: File to be decompressed
    :param outfile: Output file for decompressed contents to be saved
    :param verbose: set to True for printing console outputs
    :return: name and path of the output file
    """
    with open(inp_file, "rb") as f:
        inp: bytes = f.read()
    decomp_var = decompress_bytes(inp, verbose=verbose)
    if outfile is None:
        outfile = inp_file[:-4] if inp_file[-4:].lower() == ".hac" else inp_file
    with open(f"{outfile}", "wb") as f:
        f.write(decomp_var)
    return outfile


def decompress(inp: CompData, outfile: Optional[str] = None, verbose=False):
    """
    decompress(inp: CompData, outfile: Optional[str] = None, verbose=False):

    Decompress bytearray data or contents of a file

    :param inp: either bytearray compressed data or the filename containing the
                data
    :param outfile: name of the output file name (optional)
    :param verbose: set to True for printing console outputs
    :return: either decompressed bytearray data or name of decompressed output
            file
    """
    if isinstance(inp.data, bytearray):
        return decompress_bytes(inp.data, verbose=verbose)
    elif isinstance(inp.data, str):
        return decompress_file(inp.data, outfile=outfile, verbose=verbose)
    else:
        raise TypeError(f"inp.data is of type {type(inp.data)}")
