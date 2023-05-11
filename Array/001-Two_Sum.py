"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

#Brute force way (Python):
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for l in range(i+1,len(nums)):
                if nums[i]+nums[l] == target:
                    return i,l
                  
#Optimal way (using hashmap) (Python):
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            remainder = target - nums[i]
            if remainder in num_map:
                return i,num_map[remainder]
            num_map[num] = i

#Brute force way (Javascript) :
var twoSum = function(nums, target) {
    for (let idx1 = 0; idx1 < nums.length; idx1++) {
        for (let idx2 = idx1+1; idx2 < nums.length; idx2++) {
            if (nums[idx1] + nums[idx2] == target) {
                return [idx1,idx2]
            }
        }
    }
};

#Optimal way using hasmap (Javascript) :
var twoSum = function(nums, target) {
    const numMap = new Map()

    for (idx = 0; idx < nums.length; idx++) {
        const remainder = target - nums[idx]
        if (numMap.has(remainder)) {
            return [numMap.get(remainder), idx]
        }
        numMap.set(nums[idx], idx)
    }
};
