#! /usr/bin/env python3
# coding: utf-8

import unittest

# Two Sum My Submissions Question Solution

# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

# 316 ms

# 实现思路：
# 循环列表中的元素，用目标减去该元素结果保存在新的列表中。

def two_sum(nums, target):
	"""
	nums是无序数组
	"""
	result = []
	for i in range(0, len(nums)):
		if i> 0 and nums[i] in result:
			return result.index(nums[i])+1, i+1

		result.append(target-nums[i])


class Mytest(unittest.TestCase):
	def test_two_sum(self):
		self.assertEqual(two_sum([3,2,4], 6), (2,3))
		self.assertEqual(two_sum([-1,-2,-3,-4,-5,-6], -8), (3, 5))


if __name__ == "__main__":
	unittest.main()
