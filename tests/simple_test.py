import unittest

from src.huffpress.decompress import decompress_string
from src.huffpress.compress import compress_string


class TestHuffPress(unittest.TestCase):
    def test_string1(self):
        in_txt = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
        self.assertEqual(test_string(in_txt), True)

    def test_string2(self):
        in_txt = "AABBCC"
        self.assertEqual(test_string(in_txt), True)

    def test_string3(self):
        in_txt = "AAA"
        self.assertEqual(test_string(in_txt), True)

    def test_string4(self):
        in_txt = "A"
        self.assertEqual(test_string(in_txt), True)


def test_string(inp_txt):
    comp = compress_string(inp_txt)
    decomp = decompress_string(comp)
    dec_txt = "".join(map(chr, list(decomp)))
    return inp_txt == dec_txt
