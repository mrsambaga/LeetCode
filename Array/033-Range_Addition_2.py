"""
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
Count and return the number of maximum integers in the matrix after performing all the operations.

Example :
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
"""

class Solution(object):
    def maxCount(self, m, n, ops):
        min_row, min_col = m, n
        for x in ops:
            if x[0] < min_row :
                min_row = x[0]
            if x[1] < min_col :
                min_col = x[1]
        return min_row * min_col
      
"""
For this problem, we can track the smallest number of row and smallest number of col for every operation because it will contain the maximum number of affected by sum of 1.
"""
