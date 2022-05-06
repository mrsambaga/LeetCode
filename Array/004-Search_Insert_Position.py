"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

example :
Input: nums = [1,3,5,6], target = 5
Output: 2
"""

#Normal solution :
class Solution(object):
    def searchInsert(self, nums, target):
        for i,num in enumerate(nums):
            if num == target or num >= target:
                return i
            elif i == len(nums)-1:
                return i+1
              
#Optimal solution (using binary search) :
class Solution(object):
  def searchInsert(self, nums, target):
      low, high = 0, len(nums)
      while low<high :
          mid = (low+high)//2
          if nums[mid] == target:
              return mid
          elif nums[mid] < target:
              low = mid + 1
          else:
              high = mid
      return low
      
"""
The optimal solution is using binary search to cut down time needed to search the target. The binary search will divide array section by 2 and then searching
the target by either above or below the midpoint of array. This process done periodically until the low and high point of array are become identic or while low < high.
"""
