"""
You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.
You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

Return an array result of length 2 where:

result[0] is the total number of lines.
result[1] is the width of the last line in pixels.

Example :
Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
Output: [3,60]
Explanation: You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.
"""

class Solution(object):
    def numberOfLines(self, widths, s):
        lines, width = 0, 0
        for i,letter in enumerate(s):
            if width + widths[ord(letter)-ord('a')] <= 100 :
                width += widths[ord(letter)-ord('a')]
            else :
                lines += 1
                width = 0
                width += widths[ord(letter)-ord('a')]
        return [lines+1, width]
      
"""
For this problem we can solve it by tracking the number of current width and lines with 2 variable. To map between the number and the corresponding width we can use
ord() function to create a numerical representation of a char.
"""
