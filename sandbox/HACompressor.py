#!/usr/bin/env python
# coding: utf-8

# # Huffman-Ahmad compressor

# In[1]:


from collections import Counter
from tqdm import tqdm
import os
from enum import Enum
import json
import filecmp
from shutil import copyfile


# In[2]:


class HuffNode(object):
    def __init__(self, term: str, freq: int, left_child=None, right_child=None):
        self.term = term
        self.freq = freq
        self.left_child = left_child
        self.right_child = right_child
        
    @property
    def is_leaf(self):
        return (self.left_child is None) and (self.right_child is None)


# In[3]:


def calc_term_freq(data):
    dc = Counter(data)
    return dict(dc)


# In[4]:


def build_leaves(term_freq: dict, verbose=False):
    return {k: (v, HuffNode(k, v)) for k, v in tqdm(term_freq.items(), disable=not verbose)}


# In[5]:


def sort_tree(tree: dict):
    term_freq = sorted(tree.items(), key=lambda pair: pair[1][0], reverse=False)
    return term_freq 


# In[6]:


def build_tree(leaves: list, verbose=False):
    start_len = len(leaves)
    with tqdm(total=start_len - 1, disable=not verbose) as tbar:        
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


# In[7]:


def print_node(node: HuffNode):
    print(f"Term: {node.term}, Freq: {node.freq}")
    if node.left_child is not None:
        print("\nLeft child:")
        print_node(node.left_child)
    if node.right_child is not None:
        print("\nRight child:")
        print_node(node.right_child)


# In[8]:


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


# In[9]:


def encode_all(leaves: dict, final_tree: HuffNode, verbose=False):
    terms = leaves.keys()
    res = {}
    for term in tqdm(terms, disable=not verbose):
        res.update(encode(term, final_tree))
    return res


# In[10]:


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


# In[11]:


def create_huff_sequence(huff: dict, itxt, verbose=False):
    new_str = ""
    for i in tqdm(itxt, disable=not verbose):
        new_str += huff[i]
    rem = 8 - (len(new_str) % 8)
    new_str += "0" * rem
    return rem, new_str


# In[12]:


def dec_to_bin(num: int):
    out_bin = []
    while num > 0:
        out_bin += [num % 2]
        num //= 2
    out_bin.reverse()
    return out_bin


# In[13]:


def bin_to_dec(in_bin: list):
    in_bin.reverse()
    res = 0
    for i, x in enumerate(in_bin):
        res += x * (2 ** i)
    return res


# In[14]:


def create_final_sequence(huff_seq: tuple, verbose=False):
    if verbose:
        print("Generating final sequence")
    bin_rem = "".join(list(map(str, dec_to_bin(huff_seq[0]))))
    bin_rem = bin_rem.rjust(8, "0")
    data = bin_rem + huff_seq[1]
    return data


# In[15]:


def create_seq_bins(final_seq: str, verbose=False):
    res = []
    fin = len(final_seq) // 8
    for i in tqdm(range(fin), disable=not verbose):
        start = (i * 8)
        end = (i + 1) * 8
        res.append(final_seq[start:end])
    return res


# In[16]:


def create_seq_chars(final_bins, verbose=False):
    res = []
    for fbin in tqdm(final_bins, disable=not verbose):
        val = bin_to_dec(list(map(int, list(fbin))))
        # final_val = chr(val)
        res.append(val)
    return bytearray(res)


# In[17]:


def add_huff_map(final_seq, huff_map: dict):
    huff_bytes = [ord(x) for x in list(json.dumps(huff_map).replace(chr(32), ""))]
    huff_array = bytearray(huff_bytes)
    huff_len = list(map(lambda x: ord(str(x)), dec_to_bin(len(huff_array))))
    final_res = final_seq + huff_array + bytearray(huff_len)
    return final_res


# In[18]:


def compress_bytes(inp_st, verbose=False):
    huff, mtree = create_huff_tree(inp_st, verbose=verbose)
    huff_seq = create_huff_sequence(huff, inp_st, verbose=verbose)
    final_seq = create_final_sequence(huff_seq, verbose=verbose)
    seq_bins = create_seq_bins(final_seq, verbose=verbose)
    final_res = create_seq_chars(seq_bins, verbose=verbose)
    app_res = add_huff_map(final_res, huff)
    
    return app_res


# In[19]:


def compress_string(inp_st: str, verbose=False):
    inp_bytes = bytearray([ord(x) for x in list(inp_st)])
    return compress_bytes(inp_bytes, verbose=verbose)


# In[20]:


compress_string("Hello World")


# In[21]:


class CompressMode(Enum):
    DEFAULT = 0
    FILE = 1
    STRING = 2


# In[22]:


def compress_file(inp_file: str, verbose=False):
    inp_str = ""
    with open(inp_file, "rb") as f:
        inp_str = f.read()
    comp_str = compress_bytes(inp_str, verbose=verbose)
    outfile = f"{inp_file}.hac"
    with open(outfile, "wb") as f:
        f.write(comp_str)
    return outfile


# In[23]:


def compress(inp, verbose=False, mode=CompressMode.DEFAULT):
    if not isinstance(inp, str):
        raise TypeError("input must be a string: either a filename including path OR a text.")
    else:
        if (mode is not CompressMode.STRING) and os.path.exists(inp):
            return compress_file(inp, verbose=verbose)
        else:
            return compress_string(inp, verbose=verbose)


# In[24]:


input_text = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
ppp = compress(input_text, verbose=True)
ppp, len(ppp), len(input_text)


# In[25]:


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


# In[26]:


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


# In[27]:


def extract_huff_map(inp_str):
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
    try:
        huff_map = {int(k): v for k, v in json.loads(bytearray(huff_dic_str)).items()}
    except:
        import pdb
        pdb.set_trace()
    return huff_map, len_of_len + len(huff_dic_str)


# In[28]:


extract_huff_map(ppp)


# In[29]:


def decompress_string(inp_str):
    print("Extracting Huffman Tree")
    huff_map, rem = extract_huff_map(inp_str)
    inp_str = inp_str[:-rem]
    print("Reversing final sequence")
    rev_seq = reverse_final_sequence(inp_str)
    print("Reversing Huffman sequence")
    res = reverse_huff_sequence(huff_map, rev_seq)    
    return res


# In[30]:


decomp_text = decompress_string(ppp)
decomp_text


# In[31]:


"".join(map(chr, list(decomp_text))) == input_text


# In[32]:


def decompress_file(inp_file):
    with open(inp_file, "rb") as f:
        inp = f.read()
    decomp = decompress_string(inp)
    inp_file = inp_file[:-4] if inp_file[-4:].lower() == ".hac" else inp_file
    with open(f"{inp_file}", "wb") as f:
        f.write(decomp)
    return inp_file


# In[33]:


def test_compress(filename):
    copyfile(filename, f"{filename}.bak")
    compress(filename, verbose=True)
    decompress_file(f"{filename}.hac")
    print("COMPARISON IDENTICAL: " + str(filecmp.cmp(f"{filename}.bak", filename)))
    print(os.stat(filename))
    print(os.stat(f"{filename}.hac"))


# In[34]:


test_compress("d.txt")
test_compress("i.txt")
test_compress("j.txt")
test_compress("u.exe")


# # 16-bit testing

# In[35]:


s= 'Hello, World!'
codeList = list()
for c in s:
    codeList.append(ord(c))

print(codeList)

if len(codeList)%2 > 0:
    codeList.append(0)

finalList = list()
for d in range(0,len(codeList)-1, 2):
    finalList.append(codeList[d]*256+codeList[d+1])

print(finalList)


# In[36]:


s= 'Hello, l,mzn v0iwujgi0234jg398ghjioewrnge83hgoierhg90ehrgjsdnviwejhgwpegja;sfjq9i0jfkle weipgf weigji0eguj w90geujWorld!'
codeList = [ord(c) for c in s]    
if len(codeList)%2 > 0:    codeList.append(0)
finalList = [codeList[d]*256+codeList[d+1] for d in range(0,len(codeList)-1,2)]

print(codeList)
print(finalList)


# In[37]:


from array import array


# In[38]:


array(s[0])


# In[39]:


import struct


# In[40]:


struct.pack('H', 8787)


# In[41]:


qw = list(map(lambda x: struct.pack('H', x), finalList))
qw


# In[42]:


with open("hello.hac", "wb") as ert:
    for iop in finalList:
        ert.write(struct.pack('H', iop))


# In[43]:


import time
for i in tqdm(range(10), disable=True):
    time.sleep(0.1)


# In[ ]:




