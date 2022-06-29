"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example :
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

class Solution(object):
    def climbStairs(self, n):
        if n < 3 :
            return n
        else:
            prev = 1
            now = 2
            for i in range(3,n+1):
                now, prev = now+prev, now
            return now
          
"""
This problem is like solving fibonacci. Basically, if we know the number of way to climb n-1 stairs and n-2 stairs, we can count the number of way to climb n stairs is
by n-1 way + n-2 way.
"""
