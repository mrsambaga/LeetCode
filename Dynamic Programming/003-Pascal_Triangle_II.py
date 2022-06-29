"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example :
Input: rowIndex = 3
Output: [1,3,3,1]
"""

class Solution(object):
    def getRow(self, rowIndex):
        row = [[1]]
        for i in range(1,rowIndex+1):
            row += [map(lambda x,y: x+y, row[i-1] + [0], [0] + row[i-1])]
        return row[rowIndex]
      
"""
This problem is same as pascal triangle 1 problem. We can return the specific row by putting rowIndex in the final array.
"""
