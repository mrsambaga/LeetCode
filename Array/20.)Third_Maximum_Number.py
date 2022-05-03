"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example :
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
"""

class Solution(object):
    def thirdMax(self, nums):
        maximum = []
        setNums = set(nums)
        for x in range(3):
            if len(setNums) > 0:
                maximum.append(max(setNums))
                setNums.remove(max(setNums))
            else:
                return maximum[0]
        return maximum[-1]
      
"""
For this problem we can remove the duplicate numbers in the list by casting it to set. Then, we can find the maximum and then remove the maximum. Do it 3 times to
get the 3rd maximum number. If the length of set less than 3, return the largest number of set because the 3rd maximum doesnt exist.
"""
