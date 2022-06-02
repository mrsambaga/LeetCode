"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example :
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
"""

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = re.findall(r'\w+', paragraph.lower())
        words = {}
        for word in paragraph:
            if word not in banned:
                if word not in words.keys():
                    words[word] = 1
                else :
                    words[word] += 1
        return max(words, key=words.get)
      
#Optimal Solution (by : lee215)
class Solution(object):
    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
      
"""
For this problem, we have to extract all of the word from paragraph and removing all of the special characters in that word. We can achieve this by using regex.
re.findall(r'\w+', paragraph.lower()) will only extract alphabet in the every word and store it in the list (so we dont have to use split() anymore). Then, we can count
every word occurance and find the most frequent one. We can do this efficiently using Counter module which basically count occurence of every word. Then, we can
use most_common() to find word with the most frequent occurence.
"""

