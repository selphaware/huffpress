import json
import os

from tqdm import tqdm

from src.huffpress.generic import dec_to_bin, bin_to_dec, Mode


def reverse_final_sequence(bstr, verbose=False):
    if verbose:
        print("Reversing final sequence")
    data = list(bstr)
    rem = data[0]
    data = data[1:]
    fbin = ""
    for dec in tqdm(data, disable=not verbose):
        dbin = dec_to_bin(dec)
        vbin = "".join(list(map(str, dbin))).rjust(8, "0")
        fbin += vbin
    fbin = fbin[:-rem]
    return fbin


def reverse_huff_sequence(huff: dict, seq: str, verbose=False):
    if verbose:
        print("Reversing Huffman sequence")
    term = ""
    res = []
    huff = {v: k for k, v in huff.items()}
    for sq in tqdm(seq, disable=not verbose):
        term += sq
        val = huff.get(term)
        if val is not None:
            res.append(val)
            term = ""
    return bytearray(res)


def extract_huff_map(inp_str, verbose=False):
    if verbose:
        print("Extracting Huffman Tree")
    rev_str = list(inp_str)
    rev_str.reverse()
    rev_bytes = bytearray(rev_str)
    huff_len_bytes = []
    for r in rev_bytes:
        if r == ord('}'):
            break
        huff_len_bytes.append(r)
    huff_len_bytes.reverse()
    huff_len = bin_to_dec(list(map(lambda x: int(chr(x)), huff_len_bytes)))
    len_of_len = len(huff_len_bytes)
    huff_dic_str = inp_str[-(huff_len + len_of_len): -len_of_len]
    huff_map = {int(k): v for k, v in json.loads(bytearray(huff_dic_str)).items()}
    return huff_map, len_of_len + len(huff_dic_str)


def decompress_string(inp_str, verbose=False):
    huff_map, rem = extract_huff_map(inp_str, verbose=verbose)
    inp_str = inp_str[:-rem]
    rev_seq = reverse_final_sequence(inp_str, verbose=verbose)
    res = reverse_huff_sequence(huff_map, rev_seq, verbose=verbose)
    return res


def decompress_file(inp_file, outfile=None, verbose=False):
    with open(inp_file, "rb") as f:
        inp = f.read()
    decomp = decompress_string(inp, verbose=verbose)
    if outfile is None:
        outfile = inp_file[:-4] if inp_file[-4:].lower() == ".hac" else inp_file
    with open(f"{outfile}", "wb") as f:
        f.write(decomp)
    return outfile


def decompress(inp, outfile=None, verbose=False):
    if (not isinstance(inp, bytearray)) and (not isinstance(inp, str)):
        raise TypeError("input must be a string or bytes: "
                        "either a filename including path OR a compressed binary text.")
    else:
        if isinstance(inp, bytearray):
            return decompress_string(inp, verbose=verbose)
        else:
            return decompress_file(inp, outfile=outfile, verbose=verbose)
