"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example :
Input: nums = [1,2,3]
Output: 6
"""

class Solution(object):
    def maximumProduct(self, nums):
        nums = sorted(nums)
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
      
"""
For this problem we can sort the array and then compare between the first 2 element + the last element with the last 3 element. We compare the first 2 element +
the last element because there's a chance that the first 2 element is negative element that are bigger element than the last element.
"""
