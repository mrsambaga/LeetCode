"""
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. 
More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. 
If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.
You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.
Return the total number of seconds that Ashe is poisoned.

Example :
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        total = 0
        for i in range(len(timeSeries)):
            if i < len(timeSeries)-1 and timeSeries[i+1] <= timeSeries[i] + duration - 1:
                total += timeSeries[i+1] - timeSeries[i]
            else :
                total += duration
        return total

"""
This problem is fairly simple. All he had to do is to check if the next time teemo hit exceed the current poison duration or not. If not return add the duration
to the cumulative duration. If yes, the add the interval between current attack and next attack to the cumulative duration.
"""
