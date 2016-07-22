# -*-coding: utf-8 -*-

"""
Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# 获取字符串S最大回文子字符串。S最大长度为1000。

>>> 'abcdefghijklmnmlkjihopqrst'
'hijklmnmlkjih'

思路：对于长度为N的候选字符串，我们需要在每一个可能的中心点进行检测以判断是否构成回文字符串，这样的中心点一共有2N-1个(2N-1=N-1 + N)。
检测的具体办法是，从中心开始向两端展开，观察两端的字符是否相同

"""

import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s
        mp = ''  # 最大回文字符串
        mp_length = len(mp)
        for i in range(0, 2*length-1):
            _prev, _next = i/2, i/2 + 1 if i % 2 == 1 else i/2
            index = 0
            while _prev-index >= 0 and _next+index < length and s[_prev-index] == s[_next+index]:
                p_length = len(s[_prev-index:_next+index+1])
                if p_length > mp_length:
                    mp_length = p_length
                    mp = s[_prev-index:_next+index+1]
                index += 1
            if _next + index == length:
                break
        return mp



class TestSolution(unittest.TestCase):
    def test_longestPalindrome(self):
        self.assertEqual(Solution().longestPalindrome('abcdefghijklmnmlkjihopqrst'), 'hijklmnmlkjih')
        self.assertEqual(Solution().longestPalindrome('1234565412421242'), '2421242')
        self.assertEqual(Solution().longestPalindrome('abbc'), 'bb')
        self.assertEqual(Solution().longestPalindrome('abb'), 'bb')
        self.assertEqual(Solution().longestPalindrome('bbc'), 'bb')
        self.assertEqual(Solution().longestPalindrome('ccc'), 'ccc')
        self.assertEqual(Solution().longestPalindrome('aaaa'), 'aaaa')
        self.assertEqual(Solution().longestPalindrome('abccba'), 'abccba')


if __name__ == '__main__':
    unittest.main()
