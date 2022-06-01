"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

"""

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        translate = []
        for word in words:
            x = ""
            for letter in word:
                x += code[ord(letter)-ord('a')]
            translate.append(x)
        
        return len(set(translate))
      
"""
For this problem, we can use nested loops where we iterate over word, then iterate over letter in that word. We translate every letter to the corresponding code. We can
map easily using ord(letter)-ord('a') to get the numerical representation of char and instantly get the index position of that char in list of a-z. For example :
ord('b') is 98 and ord('a') is 97 so by subtracting ord(b) and ord(a) we get 1 which is the index of code b (code[1] = "-..."). Then, we return the length of translated
word set to find total unique combination.
"""
