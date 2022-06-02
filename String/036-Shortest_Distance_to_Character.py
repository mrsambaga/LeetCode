"""
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Example :
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
"""

#Optimal solution (by : lee215) : 
class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        res = [0 if ch == c else n for ch in s]
        for i in range(1, n):
            res[i] = min(res[i], res[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            res[i] = min(res[i], res[i + 1] + 1)
        return res
      
"""
For optimal solution, we can use double pointer to find the distance between ch to c from character on the right and distance between ch to c from from character on the left.
We can compare both of them and find the shortest one. For example : in 'accccbcca', if we want to calculate the distance between 'b' to 'a' we can find the distance from
the left which is 'accccb' with distance of 5. Turns out, if we compare the distance from the right, 'bcca' we get smaller distance which is 3.
"""

