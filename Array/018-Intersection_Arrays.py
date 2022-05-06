"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example :
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
      
"""
For this problem, we can use set to remove duplicate in the array and use 'and' operand to create the element that exist in both arrays.
"""
