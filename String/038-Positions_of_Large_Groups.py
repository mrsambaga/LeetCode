"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].
A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index.

Example :
Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
"""

class Solution(object):
    def largeGroupPositions(self, s):
        start, end, curr = 0,0,s[0]
        intervals = []
        for i,ch in enumerate(s):
            if ch != curr :
                end = i-1
                if end-start >= 2:
                    intervals.append([start,end])
                start = i
                curr = ch
            if i == len(s)-1:
                end = i
                if end-start >= 2:
                    intervals.append([start,end])
        return intervals
      
#Optimal solution (by : lee215) : 
class Solution(object):
    def largeGroupPositions(self, s):
        i, j, N = 0, 0, len(S)
        res = []
        while i < N:
            while j < N and S[j] == S[i]: j += 1
            if j - i >= 3: res.append([i, j - 1])
            i = j
        return res
      
"""
For this problem, both solution has similar concept. We need 2 pointer to keep the beginning and end of range, append the range to list if end-begin is 3 or more. In optimal
solution, we can use while loop to add index of end 1 by 1 until it reach different letter. If it reach different character, perform calculation, append, and define
new beginning. Repeat the process until we reach length of string. This code is much more simple than using for loops.
"""
      
