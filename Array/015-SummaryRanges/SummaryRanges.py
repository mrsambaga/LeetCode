"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Example :
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""

#First solution
class Solution(object):
    def summaryRanges(self, nums):
        start, finish = 0,0
        out = []
        for x in range(len(nums)):
            if x>0 and nums[x] != nums[x-1] + 1:
                finish = x-1
                if finish == start:
                    out.append(str(nums[start]))
                    start = x
                else :
                    out.append(str(nums[start]) + "->" + str(nums[finish]))
                    start = x
            if x == len(nums)-1 and start == x:
                out.append(str(nums[start]))
            elif x == len(nums)-1 and start != x :
                out.append(str(nums[start]) + "->" + str(nums[len(nums)-1]))
        return out

#Optimal solution by chichi_x
class Solution(object):
    def summaryRanges(self, nums):
        res = []
        for i in nums:
            if res and res[-1][1] == i-1:
                res[-1][1] = i
            else:
                res.append([i,i])
        return [str(x)+"->"+str(y) if x!=y else str(x) for x,y in res]
  
"""
For this problem, we can create a list to store all the ranges. Basically, we're going to store range with same number (x,x) for the beginning and then update the 2nd
element (the end range) if the element of nums is in range. If not, we're going to append new range with same number(x,x). If the element in range is the same number, that mean
the range is 0 so we print that number. If the element in range is different, that mean the range is > 0 and we print "x->y". 
"""
