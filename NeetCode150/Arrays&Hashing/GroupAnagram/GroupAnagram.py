"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

class Solution(object):
    def groupAnagrams(self, strs):
        strsMap = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in strsMap :
                strsMap[sortedS].append(s)
            else :
                strsMap[sortedS] = [s]
        return list(strsMap.values())
      
"""
For this problem, we can use hash map to map all the sorted string and make an array of string. We can sort the anagram string to 
make it the same, so we can add the corresponding string if it is a certain sorted string as a key in dictionary. Then, we can convert
the dict values to list so we can return the output correctly.
"""
