"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.

Example :
Input: s = "abcde", goal = "cdeab"
Output: true
"""

class Solution(object):
    def rotateString(self, s, goal):
        return s in goal*2 and len(s) == len(goal)
      
"""
This problem is similar to repeated substring problem. We can check if B is a rotated version of A by checking if A in B + B. Example : A = 'abc' and B = 'cab', we can find 
'abc' in 'cabcab' which mean 'cab' is a rotated version of 'abc'. Now, for this problem, we must add extra condition which is checking if A and B is the same length because
the problem said the word can only be a rotation of s. So we check if both has same length to avoid multiple string such as "a" in "aa" which is false.
"""
