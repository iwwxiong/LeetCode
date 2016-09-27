# -*-coding: utf-8 -*-

"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        digit = 1
        t = x
        while t >= 10:
            t /= 10
            digit *= 10
        while digit > 0:
            if x%10 != x/digit:
                return False
            x %= digit
            x /= 10
            digit /= 100
        return True


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertEqual(Solution().isPalindrome(12321), True)
        self.assertEqual(Solution().isPalindrome(22), True)
        self.assertEqual(Solution().isPalindrome(223), False)
        self.assertEqual(Solution().isPalindrome(1001), True)
        self.assertEqual(Solution().isPalindrome(1000021), False)


if __name__ == '__main__':
    unittest.main()