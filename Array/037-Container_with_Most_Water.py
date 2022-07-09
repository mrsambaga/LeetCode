"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example :
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""

class Solution(object):
    def maxArea(self, height):
        area = 0
        start, end = 0, len(height)-1
        while start < end:
            area = max(area, min(height[start],height[end]) * (end-start))
            if height[start] > height[end]:
                end -= 1
            else :
                start += 1
        return area
      
"""
For this problem, we can solve it by update area for every iteration. We can get the maximum area by getting maximum width and maximum height thus we start iteration
from the maximum width (idx 0 and idx max). Then we update the height by checking if the left height is higher than the right height. If yes, then move 1 step to the left
(by -1 the end index). Else, move 1 step to the right (by +1 the start index). By doing this, we can get maximum height.
"""
