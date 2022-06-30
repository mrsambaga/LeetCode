"""

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
