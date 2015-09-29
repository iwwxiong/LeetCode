#! /usr/bin/env python3
# coding: utf-8


# Add Two Numbers
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# 156 ms

import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    单链表实现
    """
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    prev_decimal = 0
    # 对象赋值是引用赋值
    _result = ListNode(0)
    result = _result

    while(l1 or l2):
        count = prev_decimal
        if l1:
            count += l1.val
            l1 = l1.next

        if l2:
            count += l2.val
            l2 = l2.next

        prev_decimal = 1 if count >= 10 else 0
        result.next = ListNode(count%10)
        result = result.next

    if prev_decimal == 1:
        result.next = ListNode(1)
    result = _result.next

    return result


def add_two_numbers_list(l1, l2):
    """
    列表实现
    """
    l1_length = len(l1)
    l2_length = len(l2)

    if l1_length == 0:
        return l2

    if l2_length == 0:
        return l1

    length = l1_length if l1_length >= l2_length else l2_length
    i = 0
    prev_decimal = 0
    result = []

    def get_index(l, index):
        try:
            return l[index]
        except IndexError:
            return 0

    while(i<length):
        count = get_index(l1, i)+get_index(l2, i)+prev_decimal
        prev_decimal = 1 if count>=10 else 0
        result.append(count%10)

        if i==length-1 and prev_decimal==1:
            result.append(prev_decimal)
        i += 1

    return result


class Mytest(unittest.TestCase):
    def test_add_two_numbers_list(self):
        self.assertEqual(add_two_numbers_list([2,4,3],[5,6,4]),[7,0,8])
        self.assertEqual(add_two_numbers_list([1,2,3],[8,8,7,9,9,9]),[9,0,1,0,0,0,1])

    def test_add_two_numbers(self):
    	l1 = ListNode(1)
    	l1.next = ListNode(8)
    	l2 = ListNode(0)
    	self.assertEqual(add_two_numbers(l1, l2).val, 1)
    	self.assertEqual(add_two_numbers(l1, l2).next.val, 8)


if __name__ == '__main__':
    unittest.main()
