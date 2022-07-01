"""
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.

Example :
Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
"""

class Solution(object):
    def divisorGame(self, n):
        return n % 2 == 0
      
"""
Alice will always win if she start with even number. She can subtract the number by 1 every turn and leaving odd number to the opponent. Odd number can only be subtracted
by odd number so if it get subtracted it will result in smaller even number. As the game goes on, eventually Alice will end up in the smallest even number (2) and will
win the game by subtracting it by 1.
"""
