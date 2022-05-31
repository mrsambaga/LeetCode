"""
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        count0, count1 = 0, 0
        group = []
        ans = 0
        for i in range(len(s)):
            if s[i] == '0' and count1 == 0:
                count0 += 1
            elif s[i] =='1' and count0 == 0:
                count1 += 1
            elif s[i] == '0' and count1 != 0:
                count0 += 1
                group.append(count1)
                count1 = 0
            elif s[i] =='1' and count0 != 0:
                count1 += 1
                group.append(count0)
                count0 = 0
            if i == len(s)-1 and count0 != 0:
                group.append(count0)
            elif i == len(s)-1 and count1 != 0:
                group.append(count1)
                
        for i in range(1, len(group)) :
            ans += min(group[i], group[i-1])
            
#Optimal Solution (by : lee215)
class Solution(object):
    def countBinarySubstrings(self, s):
        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        return sum(min(a, b) for a, b in zip(s, s[1:]))
      
"""
To solve this problem, we have to count group of 1 or 0 in string and put it in a list. For example : 11001110000 can be put as [2, 2, 3, 4]. Then, for every group,
we can find the minimum between each other, for example 11 and 00 is 2, 2 so the minimum is 2. We do this because the maximum combination that can be made between groups is
the minimum number of group : 11 00 (min 2) has combination of 1100 and 10 and 00111 (min 2) has combination of 0011 and 01. In my answer, im having a trouble in counting
the group of 1 or 0 so i use for loop and a lot of if statements. In optimal solution, the clever way to do is is by changing '01' to '0 1' and '10' to '1 0'. Basically,
it give a space between groups so we can use split to instantly separate each group and count the length of it with len.
"""
