import unittest

from tests.test_funcs import string_test, decorator_comp_test, decorator_decomp_test, print_test
from tests.test_const import LONG_TEXT


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
        print_res, actual = print_test("A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED")
        self.assertEqual(print_res, actual)
