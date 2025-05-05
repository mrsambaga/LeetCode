"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0
    
        for num in nums:
            if num-1 not in numSet :
                length = 1
                while (num+length) in numSet:
                    length += 1
                if length > longest :
                    longest = length
        return longest
      
"""
For this problem we can break down the array into a subset of consecutive number then checking the longest subset. 
we can start building the subset by checking if a smaller element (num-1) is exist in the set for a specific element. 
If not, then its the smallest element and the start of the subset. Then, we continue checking if the
next element (num+length) is exist until we get the longest consecutive sequence. The checking process takes constant O(1) time complexity
since we used hash map, so the whole algorithm take roughly O(n) time complexity.
"""
