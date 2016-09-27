.. _palindromeNumber:

Palindrome Number
------------------

Determine whether an integer is a palindrome. Do this without extra space.

判断整数是否是回文。

    >>> 12321
    True
    >>> 223
    False

**实现思路**

    1. 负数直接返回False
    2. 个位正整数直接返回True
    3. 循环对比整数首位是否相等。

**代码**

    .. literalinclude:: ../../src/palindromeNumber.py
        :language: python