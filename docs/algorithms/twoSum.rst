.. _Two Sum:

Two Sum
---------

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

    >>> nums = [2, 7, 11, 15]
    >>> target = 9
    >>> nums[0] + nums[1] == target
    True
    >>> return [0, 1]

给定一个整型数组，找出能相加起来等于一个特定目标数字的两个数。函数 ``twoSum`` 返回这两个相加起来等于目标值的数字的索引，且 ``index1`` 必须小于 ``index2`` 。

**解题思路**

    循环列表中的元素，用目标减去该元素结果保存在新的列表中。

**代码**

    .. literalinclude:: ../../src/twoSum.py
        :language: python
