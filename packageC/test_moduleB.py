#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

class TestCaseB(unittest.TestCase):

    def test_case_b_1(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_case_b_2(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def case_b_3(self):
        # 不會被 unittest 執行
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
