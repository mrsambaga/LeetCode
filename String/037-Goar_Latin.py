"""
You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat Latin.

Example :
Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
"""

class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = ['a', 'e','i','o','u','A','I','U','E','O']
        sen = sentence.split()
        for i,word in enumerate(sen):
            if word[0] in vowels:
                sen[i] = word + 'ma' + ((1+i)*'a')
            else :
                sen[i] = word[1:] + word[0] + 'ma' + ((1+i)*'a')
        return ' '.join(sen)
      
"""
This problem is fairly simple. We can create array of vowels and iterate every word & check if the first letter is vowels. Then, we can use array manipulation to append "ma", add "a",
and move the first word to the end.
"""
