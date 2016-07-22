# -*-coding: utf-8 -*-

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
"""

import unittest


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if length <= 2:
            return s
        if numRows <= 1:
            return s
        if length == numRows:
            return s

        t = 0
        r = [[] for x in range(numRows)]
        for index, item in enumerate(s):
            if t * (2*numRows - 2) == index:
                t += 1
            i = index - (t-1)*(2*numRows-2) if index - (t-1)*(2*numRows-2) <= (numRows - 1) else abs(index-t*(2*numRows-2))
            r[i].append(item)
        # return ''.join(reduce(lambda x, y: x + y, r))
        return ''.join([''.join(m) for m in r])


class SolutionTest(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(Solution().convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        self.assertEqual(Solution().convert('0123456789', 4), '0615724839')


if __name__ == '__main__':
    unittest.main()
