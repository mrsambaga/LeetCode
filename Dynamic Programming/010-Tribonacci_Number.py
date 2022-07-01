"""
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""

class Solution(object):
    def tribonacci(self, n):
        num = [0,1,1]
        if n < 3:
            return num[n]
        else :
            for i in range(3,n+1):
                num[0],num[1],num[2] = num[1], num[2], num[2]+num[1]+num[0]
            return num[2]
          
"""
This problem is basically the same as fibonacci. We just add 1 more array for the swapping formula.
"""
