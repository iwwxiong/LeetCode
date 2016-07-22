.. _addTwoNumbers:

Add Two Numbers
-----------------

You are given two linked lists representing two non-negative numbers.

The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    >>> (2, 4, 3) + (5, 6, 4)
    (7, 0, 8)

给定两个非负整数单链表，将两个单链表代表的整数相加，并返回结果单链表。

**实现思路**

    链表相加，注意10进位即可。

**代码**

    .. literalinclude:: ../../src/addTwoNumbers.py
        :language: python
