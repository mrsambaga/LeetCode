"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example :
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution(object):
    def majorityElement(self, nums):
        num = {}
        for x in nums:
            if x not in num:
                num[x] = 1
            else :
                num[x] += 1
        return max(num, key=num.get)
      
"""
For this problem, i use dictionary to keep track of the number of element that appeared in nums. Then, i use max function to find the key with maximum value in the dictionary
"""

#Other solution with sort (by OldCodingFarmer)
class Solution(object):
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]
      
"""
Since the problem specified that the majority elements always appear atleast n/2 times with n as the size of list, the majority element will always appear 
in the middle of list after it get sorted.
"""
