"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :
Input: nums = [1,2,3,1]
Output: true
"""

#Solution 1 (casting list to set)
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
      
#Solution 2 (checking with iteration
class Solution(object):
    def containsDuplicate(self, nums):
        lst = []
        for x in nums:
            if x not in lst:
                lst.append(x)
            elif x in lst:
                return True
        return False
      
"""
In this problem, we can use 2 solutions. The first solution is far more simple because we just need to remove the duplicate number from list by casting it to set. 
If the length of set is shorter than the list, that mean there are numbers who got removed.
The second solution is checking 1 by 1 and possibly can be more efficient because it can do early termination when a duplicate number is found early.
"""
