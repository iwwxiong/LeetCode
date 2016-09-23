# -*-coding: utf-8 -*-

"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""

import unittest


class Solution(object):
    max = 2147483647
    min = -2147483648
    plus = 43
    minus = 45

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None:
            return 0
        s = str.strip()
        if len(s) == 0:
            return 0
        first = ord(s[:1])
        if first != self.plus and first != self.minus and not (48 <= first <= 57):
            return 0
        sign = 1
        num = 0
        for i, j in enumerate(s):
            t = ord(j)
            if i == 0 and t == self.minus:
                sign = -1
            if i > 0 and not (48 <= t <= 57):
                break
            if t != self.plus and t != self.minus:
                num = num * 10 + int(j)
            if num * sign >= self.max:
                num = self.max
                break
            if num * sign <= self.min:
                num = -1 * self.min
                break
        return num * sign


class SolutionTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(Solution().myAtoi('123a'), 123)
        self.assertEqual(Solution().myAtoi('+234'), 234)
        self.assertEqual(Solution().myAtoi('-789'), -789)
        self.assertEqual(Solution().myAtoi('abc'), 0)
        self.assertEqual(Solution().myAtoi('-2147483648'), -2147483648)


if __name__ == '__main__':
    unittest.main()