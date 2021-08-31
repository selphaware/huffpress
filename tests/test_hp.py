import unittest

from src.huffpress.huffpress import test_compress, test_string
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

    def test_string5(self):
        in_txt = "!\"£$%^&*()_+{}:@~<>?,./;'#[]789654321/*-+\\`¬|"
        self.assertEqual(test_string(in_txt), True)

    def test_string6(self):
        in_txt = "AB"
        self.assertEqual(test_string(in_txt), True)

    def test_string7(self):
        in_txt = "        A B C D E F G       P       "
        self.assertEqual(test_string(in_txt), True)

    def test_string8(self):
        in_txt = "A "
        self.assertEqual(test_string(in_txt), True)
