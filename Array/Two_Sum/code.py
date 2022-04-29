#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

#Brute force way :

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for l in range(i+1,len(nums)):
                if nums[i]+nums[l] == target:
                    return i,l
                  
#Optimal way (using hashmap) :

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            remainder = target - nums[i]
            if remainder in num_map:
                return i,num_map[remainder]
            num_map[num] = i

