"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example :
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

class Solution(object):
    def moveZeroes(self, nums):
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1
        return nums
      
"""
For this problem we can track the index with a pointer when last time we swap the number with zero and add the index by 1 everytime we swap. 
The condition if nums[slow] != 0 is to avoid swapping between non zero number. This can happend if the list start with non zero number.
"""
