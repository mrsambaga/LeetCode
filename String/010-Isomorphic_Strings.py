"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example :
Input: s = "egg", t = "add"
Output: true
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        idx_s, idx_t = {}, {}
        s, t = list(s), list(t)

        if len(s) != len(t):
            return False
        else :
            for i in range(len(s)):
                if s[i] not in idx_s.keys():
                    idx_s[s[i]] = [i] 
                else :
                    idx_s[s[i]].append(i)
                
                if t[i] not in idx_t.keys():
                    idx_t[t[i]] = [i] 
                else :
                    idx_t[t[i]].append(i)
            
            val_s = list(idx_s.values())
            val_t = list(idx_t.values())
            
            for x in val_s:
                if x in val_t:
                    val_t.remove(x)
                else :
                    return False
            return True
          
#Optimal solution (by StefanPochmann & Numerical):
def isIsomorphic(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
  
"""
In my original answer, i was intended to map the every character (especially the duplicate char) of the string in the dictionary and then compare the list of values of both
dictionary. I want to check if they both have not only the same number of duplicate, but also same position of those duplicates. If they are the same, 
then they are isomorphic. Turns out, this can also be done by checking the length of set of zip between s,t and length of set s and length of t. This will check not only
if both string have the same duplicate but also the same location (good mapping between 2 string).
"""
  
