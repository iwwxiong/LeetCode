#! /usr/bin/env python3
# coding: utf-8

import unittest

# Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc",
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

# 981 / 981 test cases passed.
# Status: Accepted
# Runtime: 76 ms


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}
        start = -1
        sub_length = 0  #最长子字符串

        for index, value in enumerate(s):
            if value in mapping:
                start = mapping[value] if start < mapping[value] else start

            temp = index - start
            if temp > sub_length:
                sub_length = temp

            mapping[value] = index

        return sub_length


class MyTest(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('abcabcabc'), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring('abcabcabcd'), 4)
        self.assertEqual(Solution().lengthOfLongestSubstring('abcdefg'), 7)
        self.assertEqual(Solution().lengthOfLongestSubstring('abcadefnidbc'), 8)
        self.assertEqual(Solution().lengthOfLongestSubstring('pwwkew'), 3)


if __name__ == '__main__':
    unittest.main()
