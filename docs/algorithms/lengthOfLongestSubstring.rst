.. _Longest Substring Without Repeating Characters:

Longest Substring Without Repeating Characters
-------------------------------------------------

Given a string, find the length of the longest substring without repeating characters.

    >>> 'abcabcbb'
    3
    >>> 'bbbbbbbb'
    1

给定一个字符串，返回它的最长无重复子字符串长度。

**实现思路**

    遍历该字符串，更新字典中保存的最长无重复子字符串。

**代码**

    .. literalinclude:: ../../src/lengthOfLongestSubstring.py
        :language: python
