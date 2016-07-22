# -*-coding: utf-8 -*-

import unittest

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        t = 0
        if n == 0:
            nums2 = nums1
        else:
            for x in nums1:
                if x <= nums2[t]:
                    nums2.insert(t, x)
                else:
                    while x > nums2[t]:
                        t += 1
                        if t >= len(nums2):
                            break
                    nums2.insert(t, x)
        if (m + n) % 2 == 0:
            return float(nums2[(m+n)/2 - 1] + nums2[(m+n)/2]) / 2
        return float(nums2[(m+n)/2])


class SolutionTest(unittest.TestCase):
    def test_findMedianSortedArrays(self):
        self.assertEqual(Solution().findMedianSortedArrays([2,4,6,8,10], [1,3,5,7,9,10,11,12,13]), 7.5)


if __name__ == '__main__':
    a = Solution().findMedianSortedArrays([2], [])
    print a
    # unittest.main()