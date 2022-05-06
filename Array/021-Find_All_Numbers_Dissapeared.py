"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example :
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

#Solution 1 (Brute Force)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        lst = list(range(1,len(nums)+1))
        for x in set(nums):
            if x in lst:
                lst.remove(x)
        return lst
        
#Solution 2 (Optimal solution by leetcodeftw)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
            
        return [i + 1 for i, num in enumerate(nums) if num > 0]
      
"""
For optimal solution, we change every element in list to negative and make a list of that the index for the element that are positive. Since the element in nums
list are in range of 1 to n, we can turn every element into index, then we change the element of that index to negative. If we do this for all iteration,
the positive number in the list nums will point to index of missing element because no element point to that index from the earlier iteration.
"""
