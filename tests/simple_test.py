"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    main_test.py

    Testing mainly string compressions, term frequencies, and a decorator test
"""

import unittest
from tests.test_funcs import string_test, decorator_comp_test, \
    decorator_decomp_test, print_test  # type: ignore
from tests.test_const import LONG_TEXT  # type: ignore
from huffpress.huff.hfunctions import calc_term_freq  # type: ignore
from huffpress.huff.htypes import InputData, TermFreq  # type: ignore
from huffpress.auxi.basen import basen  # type: ignore
from huffpress.auxi.idict import IDict


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

    def test_basen1(self):
        val = basen(["5", "3", "6", "4", "1", "3", "5", "4", "3", "5", "4"],
                    7, 25)
        self.assertEqual(val, ["6", "A", "N", "1", "2", "H", "2"])

    def test_basen2(self):
        val = basen("UT67A001I",
                    33, 3)
        self.assertEqual(val, list("12200210110111102011011111220"))

    def test_basen3(self):
        val = basen("654",
                    10, 2)
        self.assertEqual(val, list("1010001110"))

    def test_basen4(self):
        val = basen("1101011011",
                    2, 10)
        self.assertEqual(val, list("859"))

    def test_basen5(self):
        val = basen("46894",
                    10, 16)
        self.assertEqual(val, list("B72E"))

    def test_basen6(self):
        val = basen("A872436BCD98F8D0",
                    16, 10)
        self.assertEqual(val, list("12137838076006824144"))

    def test_idict_mut(self):
        idict = IDict(False, {1: 2, "a": 3, "a-b": "hello", 2: 1.89})
        idict["yes"] = 1
        idict[3] = ["9.99", 8]
        idict["a-b"] = "goodbye"
        self.assertEqual(idict,
                         {
                             1:2, "a": 3, "a-b": "goodbye", 2: 1.89,
                             "yes": 1,
                             3: ["9.99", 8]
                         })

    def test_idict_imut(self):
        idict = IDict(True, {1: 2, "a": 3, "a-b": "hello", 2: 1.89})
        correct_error = False
        try:
            idict["yes"] = 1
        except TypeError as err:
            print(f"\nCorrect error: {err}")
            correct_error = True
        self.assertEqual(correct_error, True)
        self.assertEqual(idict, {1: 2, "a": 3, "a-b": "hello", 2: 1.89})

    def test_idict_manipulation(self):
        idict = IDict(True, {1: 2, "a": 3, "a-b": "hello", 2: 1.89})
        idict.__immutable = False  # this will not be possible
        print(f"\nDict is immutable: {idict.is_immutable}")
        self.assertEqual(idict.is_immutable, True)
        correct_error = False
        try:
            idict["yes"] = 1
        except TypeError as err:
            print(f"\nCorrect error: {err}")
            correct_error = True
        self.assertEqual(correct_error, True)
        self.assertEqual(idict, {1: 2, "a": 3, "a-b": "hello", 2: 1.89})

    def test_idict_manipulation2(self):
        idict = IDict(False, {1: 2, "a": 3, "a-b": "hello", 2: 1.89})
        idict.__immutable = True  # this will not be possible
        print(f"\nDict is immutable: {idict.is_immutable}")
        self.assertEqual(idict.is_immutable, False)
        idict["yes"] = 1
        idict[3] = ["9.99", 8]
        idict["a-b"] = "goodbye"
        self.assertEqual(idict,
                         {
                             1:2, "a": 3, "a-b": "goodbye", 2: 1.89,
                             "yes": 1,
                             3: ["9.99", 8]
                         })
