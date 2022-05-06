"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example :
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""

#Solution 1 (Brute force)
class Solution(object):
    def missingNumber(self, nums):
        lst = list(range(len(nums)+1))
        for x in nums:
            if x in lst:
                lst.remove(x)
        return lst[0]
      
#Solution 2 (Using math)
class Solution(object):
    def missingNumber(self, nums):
        x = len(nums)
        return ((x * (x+1)) // 2) - sum(nums) 
      
"""
The faster way to solve this problem is using gauss formula to find sum of consecutive numbers and subtract it with sum of the list.
"""
