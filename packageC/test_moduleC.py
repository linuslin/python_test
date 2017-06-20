#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

class TestCaseC(unittest.TestCase):

    def test_case_c_1(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def testcase_2(self):
        # 會被 unittest 執行，因為開頭有 test 關鍵字，但是比較建議 test_ 的寫法。
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def case_c_3(self):
        # 不會被 unittest 執行
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
