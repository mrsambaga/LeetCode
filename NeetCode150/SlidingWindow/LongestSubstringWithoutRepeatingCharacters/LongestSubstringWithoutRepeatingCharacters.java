package NeetCode150.SlidingWindow.LongestSubstringWithoutRepeatingCharacters;

import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        Map<String, Integer> hashStr = new HashMap<>();
        Integer maxLength = 0;
        Integer leftPointer = 0;
        String[] letters = s.split("");

        if (s.length() == 0) {
            return 0;
        }

        for (int i = 0; i < letters.length; i++) {
            if (hashStr.containsKey(letters[i])) {
                leftPointer = Math.max(leftPointer, hashStr.get(letters[i]) + 1);
            }

            hashStr.put(letters[i], i);
            maxLength = Math.max(maxLength, i - leftPointer + 1);
        }

        return maxLength;
    }
}

// This problem can be solved by using a sliding window.
// We use a hashmap to store the characters and their last index.
// We use a left pointer for the start and right pointer for the end of the window.
// We use a maxLength to keep track of the longest substring without repeating characters.
// Whenever we encounter a character that is already in the hashmap, we update the left pointer to the next character after the last occurrence of the character.
// This solution has O(n) time complexity and O(n) space complexity.


