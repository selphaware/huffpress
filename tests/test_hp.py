import unittest

from src.huffpress import test_compress
from os import remove


class TestHuffPress(unittest.TestCase):
    def test_d_txt(self):
        assert(test_compress("d.txt"), True)
        remove("d.txt.bak")
        remove("d.txt.hac")

    def test_i_txt(self):
        assert(test_compress("i.txt"), True)
        remove("i.txt.bak")
        remove("i.txt.hac")

    def test_j_txt(self):
        assert(test_compress("j.txt"), True)
        remove("j.txt.bak")
        remove("j.txt.hac")

    def test_u_exe(self):
        assert(test_compress("u.exe"), True)
        remove("u.exe.bak")
        remove("u.exe.hac")
