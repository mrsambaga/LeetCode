"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

class Solution(object):
    def generate(self, numRows):
        out = []
        for i in range(numRows):
            if len(out) == 0 :
                out.append([1])
            elif len(out) == 1:
                out.append([1,1])
            else :
                temp = [1] * (i+1)
                for l in range(1,i):
                    temp[l] = out[i-1][l-1] + out[i-1][l]
                out.append(temp)
        return out
      
#Optimal solution using map (by : sherlock321)
def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
      
"""
For optimal solution, we can add the previous line with itself but add 0 in the beginning and 0 in the end. Example for 3rd line of triangle :
110
011
---+
121
"""
