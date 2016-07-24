# -*-coding: utf-8 -*-

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

import unittest


class Solution(object):
    max = 0x7fffffff

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            return self._reverse(x)
        return -self._reverse(abs(x))

    def _reverse(self, x):
        if x < 10:
            return x
        y = 0
        while x > 0:
            y = 10 * y + x % 10 if (x % 10 > 0 or y > 0) else y
            x = x / 10
        if y > self.max:
            return 0
        return y


class SolutionTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(Solution().reverse(123), 321)
        self.assertEqual(Solution().reverse(123321), 123321)
        self.assertEqual(Solution().reverse(-123), -321)
        self.assertEqual(Solution().reverse(-100), -1)
        self.assertEqual(Solution().reverse(100), 1)
        self.assertEqual(Solution().reverse(901000), 109)
        self.assertEqual(Solution().reverse(9646324351), 0)


if __name__ == '__main__':
    unittest.main()


