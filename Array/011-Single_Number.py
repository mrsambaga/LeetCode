"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example :
Input: nums = [2,2,1]
Output: 1
"""

class Solution(object):
    def singleNumber(self, nums):
        lst = []
        for i in nums:
            if i not in lst:
                lst.append(i)
            elif i in lst:
                lst.remove(i)
        return lst[0]

"""
For this problem we can use hash method where we store the element that we encounter and remove it if we find it again in the nums list after we iterate.
"""
