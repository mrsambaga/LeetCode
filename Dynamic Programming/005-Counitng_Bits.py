"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
"""

class Solution(object):
    def countBits(self, n):
        ans = [0]
        for i in range(1,n+1):
            binary = bin(i)[2:]
            ans.append(binary.count('1'))
        return ans
      
"""
This is a brute force solution with bin function and count function. We can turn int to binary with bin() and count how many 1 in the result, then append it.
"""
