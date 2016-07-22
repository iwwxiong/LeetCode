.. _Longest Palindromic Substring:

Longest Palindromic Substring
-------------------------------

Given a string S, find the longest palindromic substring in S.

You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

    >>> 'abcdefghijklmnmlkjihopqrst'
    'hijklmnmlkjih'
    >>> 'abbc'
    'bb'
    >>> 'cccc'
    'cccc'

寻找字符串S的最长回文子字符串（字符串长度最长1000）。

**实现思路**

    对于长度为N的候选字符串，我们需要在每一个可能的中心点进行检测以判断是否构成回文字符串，这样的中心点一共有2N-1个(2N-1=N-1 + N)。
    检测的具体办法是，从中心开始向两端展开，观察两端的字符是否相同。

**代码**

    .. literalinclude:: ../../src/longestPalindrome.py
        :language: python
