"""
Given a string licensePlate and an array of strings words, find the shortest completing word in words.
A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".
Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

Example :
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.
"""

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        letters = {}
        minim = 0
        for char in licensePlate.lower():
            if char.isalpha() == True:
                if char not in letters:
                    letters[char] = 1
                else :
                    letters[char] += 1
        
        keys = list(letters.keys())
        for word in words:
            for l in range(len(keys)):
                if word.count(keys[l]) < letters[keys[l]]:
                    break
                if l == len(keys)-1:
                    if minim == 0:
                        minim = word
                    elif len(word) < len(minim):
                        minim = word   
        return minim
      
#2 Line Solution (by : rostam)
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        pc = Counter(filter(lambda x : x.isalpha(), licensePlate.lower()))
        return min([w for w in words if Counter(w) & pc == pc], key=len) 
      
"""
To solve this problem, first we have to extract all alphabet in the plate and make it lowercase. Then, check if word contain all alphabet in license plate and check if its
the same or higher occurance. If yes, store it and repeat to all words then return the smallest word. In 2 line solution, we can use Counter module to easily map
every word to a dictionary of alphabet in licese plate. Then, we can use and operator between the counter of word and the counter of license plate to find the same
alphabet. If the number of same alphabet is equal to counter of license plate, that mean all of the alphabet in licese plate are in the word so we store the word. Repeat
it again and find the smallest word.
"""
