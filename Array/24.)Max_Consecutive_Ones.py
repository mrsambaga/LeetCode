"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maximum, curr = 0,0
        
        for x in nums:
            if x == 1:
                curr += 1
            else :
                curr = 0
            if curr > maximum:
                maximum = curr
        return maximum

"""
For this problem, we can create O(n) solution by using double pointer to track the current consecutive 1 and the maximum consecutive 1.
"""
