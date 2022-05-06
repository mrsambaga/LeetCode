"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) 
for all i is maximized. Return the maximized sum.

Example :
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
"""

class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted(nums, reverse=True)
        out = 0
        for i in range(0,len(nums),2):
            out += nums[i+1]
        return out
      
"""
We can sort the array in decending order and then sum every odd index element because that will be the minimum from the pair which is the even index element.
We use sort because we get the maximum number by pairing the largest element with 2nd largest element, then 3rd largest with 4th largest, and so on.
"""
