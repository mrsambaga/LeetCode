"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""

# Solution 1 (too much code but faster O(n))
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1Map = {}
        nums2Map = {}
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                if nums1[i] in nums1Map:
                    nums1Map[nums1[i]] += 1
                else :
                    nums1Map[nums1[i]] = 1
            
            if i < len(nums2):
                if nums2[i] in nums2Map:
                    nums2Map[nums2[i]] += 1
                else :
                    nums2Map[nums2[i]] = 1

        out = []
        for num in nums1Map:
            if num in nums2Map:
                temp = [num] * min(nums1Map[num], nums2Map[num])
                out += temp
        
        return out

# Solution 2 (simpler but slower O(n^2))
class Solution(object):
    def intersect(self, nums1, nums2):
        lst = []
        for x in nums1:
            if x in nums2 and x not in lst:
                lst += [x] * min(nums1.count(x), nums2.count(x))
        return lst
      
"""
For this problem, we can store the element in another list. We can find out how many time the element appear in both arrays with count() and find the min of those 2 
numbers to make sure the elements appear that many times in both array. Then, we can append it to the list.
"""
