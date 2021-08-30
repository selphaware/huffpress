import unittest

from src.huffpress import test_compress


class TestHuffPress(unittest.TestCase):
    def test_d_txt(self):
        assert(test_compress("d.txt"), True)

    def test_i_txt(self):
        assert(test_compress("i.txt"), True)

    def test_j_txt(self):
        assert(test_compress("j.txt"), True)

    def test_u_exe(self):
        assert(test_compress("u.exe"), True)
