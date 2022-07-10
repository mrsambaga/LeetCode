"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example :
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        out = nums[0] + nums[1] + nums[2]
        nums.sort()
        for left in range(len(nums)-2):
            mid = left + 1
            right = len(nums)-1
            while mid < right:
                res = nums[left] + nums[mid] + nums[right]
                if abs(target - res) < abs(target - out):
                    out = res
                if res > target:
                    right -= 1
                elif res < target:
                    mid += 1
                else:
                    return res
        return out
      
"""
The solution of this problem is similar to the 3 sum problem. We can use 3 variable left, mid, and right as the 1st, 2nd, and 3rd element. Then, we can sum it and 
compare if the result is closer to the target than the previous one. We move 1 step to the right or left on while loop depend on the result. If the result is bigger than
the target, we move the right element 1 step to the left to get smaller number and if the result is smaller, we move mid element to the right to get bigger element.
This problem is easier than the 3 sum problem because we dont care about the avoiding duplicate.
"""
