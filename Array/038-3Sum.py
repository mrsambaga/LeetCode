"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example :

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

#Time exceeded attempt
class Solution(object):
    def threeSum(self, nums):
        out = []
        nums.sort()
        for i in range(len(nums)-1):
            temp = []
            for l in range(i+1, len(nums)):
                remainder = 0 - nums[i] - nums[l]
                if remainder in temp and [nums[i],nums[l],remainder] not in out:
                    out.append([nums[i],nums[l],remainder])
                temp.append(nums[l])
        return out
      
#Optimal solution (by : OldCodingFarmer & SailorMoons):
class Solution(object):
    def threeSum(self, nums):
      nums.sort()
      result = []
      for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
          if left > 0 and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
              continue 
          mid = left + 1 # renamed this to mid because this is the pointer that is between the left and right pointers
          right = len(nums) - 1
          while mid < right:
              curr_sum = nums[left] + nums[mid] + nums[right]
              if curr_sum < 0:
                  mid += 1 
              elif curr_sum > 0:
                  right -= 1
              else:
                  result.append([nums[left], nums[mid], nums[right]])
                  while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                      mid += 1
                  while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                      right -= 1
                  mid += 1
                  right -= 1
        return result
  
"""
The optimal solution basically use 3 variables as array index which is left as 1st element, mid as 2nd element, and right as 3rd element. The while loop basically check
the sum of left, mid, and right. If its equal to less than zero, we can move the mid element to the right by 1 because it will make the total sum bigger 
(more positive number since the array is sorted). If its more than zero, we can move the right element to the left by 1 because it will make the total sum smaller.
If its equal to 0, append it to the output then check the element if it is duplicate to the next index. If it does, skip it. This will result in avoiding duplicate.
"""
