"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
starting from 0 and 1. That is, 
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Example :
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
"""

class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        else :
            prev,now = 0,1
            for i in range(2, n+1) :
                prev,now = now, prev+now
            return now
          
"""
The solution of this problem is similar to climbing stairs problem. We can use basic fibonacci formula to update the now number(become next number) with prev+now 
and update the prev number(become now in the next iter) with now.
"""
