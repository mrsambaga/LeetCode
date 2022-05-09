"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return 
if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example :
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        if n == 0 :
            return True
        for x in range(1, len(flowerbed)-1):
            if flowerbed[x-1] == flowerbed[x] == flowerbed[x+1] == 0 :
                flowerbed[x] = 1
                n -= 1
            if n == 0:
                return True
        return False
      
"""
For this problem we can add 0 in the beginning and end of the list so we can check x-1, x, and x+1 element of list. If all of those elements are zeros, update the
x element to 1 and subtract 1 flower. If flower reach zero, that mean they all been planted without violation rule.
"""
