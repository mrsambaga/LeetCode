"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example :
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

class Solution(object):
    def generate(self, numRows):
        lst = []
        for x in range(numRows):
            lst.append([0] * (x+1))
            for y in range(x+1):
                if y == 0 :
                    lst[x][0] = 1
                elif y == x :
                    lst[x][x] = 1
                else :
                    lst[x][y] = lst[x-1][y-1] + lst[x-1][y]
        return lst
      
"""
To answer this problem, we need to understand the pattern of pascal triangle. The patter basically is 1 in every edge of list and the middle parts come's from 
the sum of same element position and element before from the last list.
"""

#Optimal solution using map (by : sherlock321)

def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
      
"""
This solution is using the strategy of adding the offset of current list to create the next list ( 1,2,1,0 + 0,1,2,1 = 1,3,3,1) and then using map & lamda 
expression to make the calculation process & list making process shorter.
"""
