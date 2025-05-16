"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up 
to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""

class Solution(object):
    def twoSum(self, numbers, target):
        startPointer = 0
        endPointer = len(numbers)-1
        
        while startPointer < endPointer:
            if numbers[startPointer] + numbers[endPointer] > target:
                endPointer -= 1
            elif numbers[startPointer] + numbers[endPointer] < target:
                startPointer += 1
            else :
                return [startPointer+1, endPointer+1]
              
"""
In this solution, we can use double pointer to get optimal solution by taking advantage of sorted array. Since the array is sorted,
we know if the start + end element is bigger than the target, we can shift the end it to the left and shift the start to the right
if the combination is less than the target.
"""
