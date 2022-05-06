"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example :
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
"""

#Solution 1 :
class Solution(object):
    def findRelativeRanks(self, score):
        sortScore = sorted(score, reverse=True)
        for x in range(len(score)):
            if sortScore.index(score[x])+1 == 1:
                score[x] = 'Gold Medal'
            elif sortScore.index(score[x])+1 == 2:
                score[x] = 'Silver Medal'
            elif sortScore.index(score[x])+1 == 3:
                score[x] = 'Bronze Medal'
            else:
                score[x] = str(sortScore.index(score[x])+1)
        return score
      
#Better solution (by : StefanPochmann)
class Solution(object):
    def findRelativeRanks(self, nums):
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(sort, rank)).get, nums)
  
"""
For the first solution, im using sorted to sort the scores in descending order, then use iteration to find the index of every element from score on score sorted.
We can create better solution with similar idea but more efficient by using map & dict. After sorting the scores & create all available ranks, zip them together and then
crete dictionary which will assign every score as keys and the sorted score as value (their respective ranks). Use map to find the ranks of every scores. 
"""
