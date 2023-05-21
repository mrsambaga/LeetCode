"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example :
Input: rowIndex = 3
Output: [1,3,3,1]
"""

class Solution(object):
    def getRow(self, rowIndex):
        lst = [[1]]
        for i in range(1,rowIndex+1):
            lst += [map(lambda x,y: x+y, [0]+lst[-1], lst[-1]+[0])]
        return lst[rowIndex]
      
"""
This problem is basically the same as pascal triangle I problem. We can use optimal solution from the last problem (adding offset of list to create next list)
and then returning only the wanted list.
"""
