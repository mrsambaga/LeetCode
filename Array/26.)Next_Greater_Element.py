"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example :
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""

#Solution 1 (Brute force)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for i,num in enumerate(nums1):
            for l in nums2[nums2.index(num)+1:]:
                if nums2.index(num)+1 < len(nums2) and l > nums2[nums2.index(num)]:
                    ans.append(l)
                    break
            else :
                ans.append(-1)
        return ans
      
#Optimal solution (using stacks, by : harshkothari410
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        d = {}
        st = []
        ans = []
        
        for x in nums2:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in nums1:
            ans.append(d.get(x, -1))
            
        return ans
      
"""
For the brute force solution, we use O(n^2) algorithm to check if the next number for every list is greater than the current number.
For the optimal solution, we can get O(n) solution by using stack. Basically, we're keeping tracks of the decresing subset and find the next greater number because
all those element in decreasing subset will have the same next greater element. We're storing the the element and index of next greater (if any) with dictionary. Then,
we map the ans by using get() to get the value of every keys in dict (the element which have next greater element) or -1 if not in dict.
"""
