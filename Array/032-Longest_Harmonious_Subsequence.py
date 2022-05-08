"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example :
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
"""

#Staightforward solution (by : awice) :
class Solution(object):
    def findLHS(self, nums):
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
        return ans

"""
For this problem, we can store the occurence of every element in list to dictionary. Then, we find out if there is x + 1 for every x in dictionary. If there is,
sum the number of occurence between the x & x+1 and store it in max. Repeat and update if we find another maximum to get longest harmonious subsequence. 
We do this because the array with difference between maximum and minimum is 1 will only contain number of x and x+1 in the array.
"""
