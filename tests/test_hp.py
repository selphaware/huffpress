import unittest

from src.huffpress import test_compress
from os import remove


class TestHuffPress(unittest.TestCase):
    def test_d_txt(self):
        self.assertEqual(test_compress("tests/files/d.txt"), True)
        remove("tests/files/d.txt.bak")
        remove("tests/files/d.txt.hac")

    def test_i_txt(self):
        self.assertEqual(test_compress("tests/files/i.txt"), True)
        remove("tests/files/i.txt.bak")
        remove("tests/files/i.txt.hac")

    def test_j_txt(self):
        self.assertEqual(test_compress("tests/files/j.txt"), True)
        remove("tests/files/j.txt.bak")
        remove("tests/files/j.txt.hac")

    def test_u_exe(self):
        self.assertEqual(test_compress("tests/files/u.exe"), True)
        remove("tests/files/u.exe.bak")
        remove("tests/files/u.exe.hac")
