package NeetCode150.SlidingWindow;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class LongestRepeatingCharacterReplacement {
    public int characterReplacement(String s, int k) {
        Integer leftPointer = 0;
        Integer rightPointer = 0;
        Integer maxLength = 0;
        Map<Character, Integer> charCount = new HashMap<>();

        while (rightPointer < s.length()) {
            charCount.put(s.charAt(rightPointer), charCount.getOrDefault(s.charAt(rightPointer), 0) + 1);

            while ((rightPointer - leftPointer + 1) - Collections.max(charCount.values()) > k) {
                charCount.put(s.charAt(leftPointer), charCount.get(s.charAt(leftPointer)) - 1);
                leftPointer++;
            }

            maxLength = Math.max(maxLength, rightPointer - leftPointer + 1);
            rightPointer++;
        }

        return maxLength;
    }
}

// For this problem, we can use sliding window to solve it. We use left and right pointer to create a window.
// We put every character in the string into a hashmap and count the number of times each character appears.
// So that we can keep track of the most frequent character in the window (since it takes less replacement).
// First we move the right pointer to the right to expand the window.
// Every iteration, we check if the length of window minus the most frequent character appears is greater than k.
// If it is, that mean the window is not valid and we move the left pointer to the right to shrink the window until it is valid.
// After that, we update the maxLength with the length of the window.
// This solution is O(n) because we only traverse the string once. Technically, it is O(26n) because the hashmap will at most have 26 characters.