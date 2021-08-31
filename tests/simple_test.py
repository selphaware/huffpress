import unittest

from huffpress.test_funcs import string_test, LONG_TEXT, decorator_comp_test, decorator_decomp_test


class TestHuffPressSimple(unittest.TestCase):
    def test_string1(self):
        in_txt = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
        self.assertEqual(string_test(in_txt), True)

    def test_string2(self):
        in_txt = "AABBCC"
        self.assertEqual(string_test(in_txt), True)

    def test_string3(self):
        in_txt = "AAA"
        self.assertEqual(string_test(in_txt), True)

    def test_string4(self):
        in_txt = "A"
        self.assertEqual(string_test(in_txt), True)

    def test_decor(self):
        bytes_data = decorator_comp_test()
        decomp_txt = decorator_decomp_test(in_var=bytes_data)
        print(f"Length Raw = {len(LONG_TEXT)}")
        print(f"Length Compressed = {len(bytes_data)}")
        print(f"Length Decompressed = {len(decomp_txt)}")
        self.assertEqual(decomp_txt, LONG_TEXT)
