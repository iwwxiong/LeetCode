.. _ZigZag Conversion:

ZigZag Conversion
------------------

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

(you may want to display this pattern in a fixed font for better legibility)

    >>> 'PAYPALISHIRING'
    'PAHNAPLSIIGYIR'
    >>> '0123456789'
    '0615724839'

给定一个字符串和行数，然后之字形转换字符串，按行输出结果。

**实现思路**
-------------

    遍历字符串，然后用保存该字符到对应行数的列表中，最后合并列表即可

**代码**
---------

    .. literalinclude:: ../../src/zigzagConvert.rst
        :language: python
