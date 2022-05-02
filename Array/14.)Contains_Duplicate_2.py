"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example :
Input: nums = [1,2,3,1], k = 3
Output: true
"""

#Solution 1 (using iteration & abs)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        lst = []
        for i,num in enumerate(nums):
            if num not in lst:
                lst.append(num)
            elif num in lst:
                if abs(i-lst.index(num)) <= k:
                    return True
                else :
                    lst[lst.index(num)] = ''
                    lst.append(num)
        return False
      
#Solution 2 (using dictionary, by : OldCodingFarmer)
def containsNearbyDuplicate(self, nums, k):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic and i - dic[num] <= k:
            return True
        dic[num] = i
    return False
  
"""
For the first solution, im storing the element in list 'lst' to keep track the element and the index so i can compute abs(i-j) <= k by accessing index of 
the element lst. The problem is, i cannot access the 2nd or more duplicate element using lst.index(num) because it will only return the first element found.
So, i have to replace it to '' so i can track the 2nd or more element using lst.index. In the 2nd solution, dictionary is used and i can update the value easily
without caring about the index which make the code much simpler.
"""
