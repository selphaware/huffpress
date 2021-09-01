import filecmp
from shutil import copyfile

from huffpress.compress import compress
from huffpress.decompress import decompress
from huffpress.decorators import comp, decomp
from huffpress.generic import Mode
from huffpress.huffman.hfunctions import create_huff_tree, print_node
from tests.test_const import LONG_TEXT, PRINT_RES_1


def string_test(inp_txt):
    comp_var = compress(inp_txt)
    decomp_var = decompress(comp_var)
    dec_txt = "".join(map(chr, list(decomp_var)))
    return inp_txt, dec_txt


def print_test(inp_txt):
    _, tree = create_huff_tree(inp_txt)
    return print_node(tree, verbose=False), PRINT_RES_1


@comp
def decorator_comp_test():
    return LONG_TEXT


@decomp("in_var")
def decorator_decomp_test(in_var):
    return in_var


def compress_test(filename, mode=Mode.DEFAULT):
    copyfile(filename, f"{filename}.bak")
    compress(filename, mode=mode, verbose=True)
    decompress(f"{filename}.hac", verbose=True)
    return filecmp.cmp(f"{filename}.bak", filename)
