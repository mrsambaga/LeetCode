"""
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. 
Also, assume that the magnitude of the robot's movement is the same for each move.

Example :
Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
"""

class Solution(object):
    def judgeCircle(self, moves):
        start=[0,0]
        for char in moves:
            if char == 'U':
                start[1] += 1
            elif char == 'D':
                start[1] -= 1
            elif char == 'R':
                start[0] += 1
            elif char == 'L':
                start[0] -= 1
        return start == [0,0]
      
"""
This problem is pretty simple. We can use 2 variable approach where the first var track the x-axis position which is left & right and second variable hold the
y-axis position which up & down. We just need to add or subtract the corresponding axis coordinate.
"""
