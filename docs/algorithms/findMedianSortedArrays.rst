.. _Median of Two Sorted Arrays:

Median of Two Sorted Arrays
----------------------------

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    >>> [1, 3]
    >>> [2]
    2.0
    >>> [1, 3]
    >>> [2, 4]
    2.5

寻找给定有序数组 ``nums1`` （长度m） 和 ``nums2`` （长度n） 。找出中位数，要求时间复杂度 :math:`O(\log (m + n))` 。

**实现思路**

    合并两个有序数组（循环其中一个数组，把值插入到另一个数组合适的位置），然后计算中位数。

**代码**

    .. literalinclude:: ../../src/findMedianSortedArrays.py
        :language: python
