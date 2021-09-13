"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    main_test.py

    Testing mainly string compressions, term frequencies, and a decorator test
"""

import unittest
# noinspection Mypy
from tests.test_funcs import string_test, decorator_comp_test, \
    decorator_decomp_test, print_test
# noinspection Mypy
from tests.test_const import LONG_TEXT
# noinspection Mypy
from huffpress.huffman.hfunctions import calc_term_freq
# noinspection Mypy
from huffpress.huffman.htypes import InputData, TermFreq


class TestHuffPressSimple(unittest.TestCase):
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

    def test_decor(self):
        bytes_data = decorator_comp_test()
        decomp_txt = decorator_decomp_test(in_var=bytes_data)
        print(f"Length Raw = {len(LONG_TEXT)}")
        print(f"Length Compressed = {len(bytes_data)}")
        print(f"Length Decompressed = {len(decomp_txt)}")
        self.assertEqual(decomp_txt, LONG_TEXT)

    def test_print(self):
        print_res, actual = print_test("A_DEAD_DAD_CEDED_A_BAD_"
                                       "BABE_A_BEADED_ABACA_BED")
        self.assertEqual(print_res, actual)

    def test_calc_termfreq(self):
        ctf = calc_term_freq(InputData(data="Hello World Hi"))
        self.assertEqual(
            ctf,
            TermFreq(tf={32: 2, 72: 2, 87: 1, 100: 1, 101: 1,
                         105: 1, 108: 3, 111: 2, 114: 1})
        )

    def test_calc_termfreq_bytes(self):
        inp_dat = b"ABCCDDDD"
        self.assertEqual([x for x in inp_dat], [65, 66, 67, 67, 68, 68, 68, 68])
        ctf = calc_term_freq(InputData(data=inp_dat))
        self.assertEqual(
            ctf,
            TermFreq(tf={65: 1, 66: 1, 67: 2, 68: 4})
        )
