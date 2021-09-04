"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    main_test.py

    Testing mainly file compressions and some string compressions
"""

import unittest
# noinspection Mypy
from tests.test_funcs import string_test, compress_test
from os import remove


class TestHuffPress(unittest.TestCase):
    def test_d_txt(self):
        self.assertEqual(compress_test("../tests/files/d.txt"), True)
        remove("../tests/files/d.txt.bak")
        remove("../tests/files/d.txt.hac")

    def test_i_txt(self):
        self.assertEqual(compress_test("../tests/files/i.txt"), True)
        remove("../tests/files/i.txt.bak")
        remove("../tests/files/i.txt.hac")

    def test_j_txt(self):
        self.assertEqual(compress_test("../tests/files/j.txt"), True)
        remove("../tests/files/j.txt.bak")
        remove("../tests/files/j.txt.hac")

    def test_u_exe(self):
        self.assertEqual(compress_test("../tests/files/u.exe"), True)
        remove("../tests/files/u.exe.bak")
        remove("../tests/files/u.exe.hac")

    def test_string1(self):
        in_txt = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
        com_dat, decom_dat = string_test(in_txt)
        self.assertEqual(com_dat, decom_dat)

    def test_string2(self):
        in_txt = "AABBCC"
        com_dat, decom_dat = string_test(in_txt)
        self.assertEqual(com_dat, decom_dat)

    def test_string3(self):
        in_txt = "AAA"
        com_dat, decom_dat = string_test(in_txt)
        self.assertEqual(com_dat, decom_dat)

    def test_string4(self):
        in_txt = "A"
        com_dat, decom_dat = string_test(in_txt)
        self.assertEqual(com_dat, decom_dat)

    def test_string5(self):
        in_txt = "!\"£$%^&*()_+{}:@~<>?,./;'#[]789654321/*-+\\`¬|"
        com_dat, decom_dat = string_test(in_txt)
        self.assertEqual(com_dat, decom_dat)

    def test_string6(self):
        in_txt = "AB"
        com_dat, decom_dat = string_test(in_txt)
        self.assertEqual(com_dat, decom_dat)

    def test_string7(self):
        in_txt = "        A B C D E F G       P       "
        com_dat, decom_dat = string_test(in_txt)
        self.assertEqual(com_dat, decom_dat)

    def test_string8(self):
        in_txt = "A "
        com_dat, decom_dat = string_test(in_txt)
        self.assertEqual(com_dat, decom_dat)
