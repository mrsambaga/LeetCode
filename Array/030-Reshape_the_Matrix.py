"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example :
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
"""

#Solution 1 (manual way)
class Solution(object):
    def matrixReshape(self, mat, r, c):
        flat = [item for sublist in mat for item in sublist]
        ans = []
        if len(flat) == r*c:
            while r > 0:
                for x in range(0,len(flat),c):
                    ans.append(flat[x:x+c])
                    r -= 1
            return ans
        else :
            return mat
          
#Solution 2 (using numpy reshape. by : StefanPochmann)
import numpy as np
class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums

"""
For this problem, theres 2 solution. The 2nd solution using numpy reshape to automaticly reshape array if possible. This solution is slower than the 1st solution.
For the  1st solution, the array is flatten at first to make it easier to extract some amount of number every iteration. 
Then, iterate as many times as row number, and append element to answer with as many element as column number every iteration.
"""
