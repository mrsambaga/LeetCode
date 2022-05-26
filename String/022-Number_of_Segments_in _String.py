"""
Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Example :
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
"""

#Solution 1
class Solution(object):
    def countSegments(self, s):
        return len(s.split())

#Solution 2 (without split)
class Solution(object):
    def countSegments(self, s):
        add = False
        ans = 0
        for x in s:
            if x != " " and add == False:
                ans += 1
                add = True
            elif x == " " :
                add = False
        return ans
      
"""
This problem is pretty easy to solve in python
"""
