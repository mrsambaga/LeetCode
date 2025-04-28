import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> result = new HashMap<>();

        for (String word : strs) {
            char[] letters = word.toCharArray();
            Arrays.sort(letters);
            String sortedWord = new String(letters);
            
            result.computeIfAbsent(sortedWord, k -> new ArrayList<>()).add(word);
        }

        return new ArrayList<>(result.values());
    }
}


// In the first solution, we can use sort algorithm to sort all the word and compare them in result map. 
// We can use compute if absent to insert a new empty list if the word is not exist in a map and then add the original word into it.
// Finally we can convert the list of string into list of list of string as the final answer.
// This solution will give time complexity about O(m * k log n) (with m as the total words, and k log n is the complexity of sort (quicksort))


class Solution2 {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> finalResult = new HashMap<>();

        for (String word : strs) {
            int[] letterCount = new int[26];

            for (char letter : word.toCharArray()) {
                letterCount[letter - 'a']++;
            }

            StringBuilder anagramMappingBuilder = new StringBuilder();
            for (int count : letterCount) {
                anagramMappingBuilder.append(Integer.toString(count));
                anagramMappingBuilder.append('#');
            }

            finalResult.computeIfAbsent(anagramMappingBuilder.toString(), k -> new ArrayList<>()).add(word);
        }

        return new ArrayList<>(finalResult.values());
    }
}

// This is an optimal solution that i found from NeetCode.
// Basically, we create an array of 26 (total alphabets), count every letter appearance, put them inside the array.
// The trick is using letterCount[letter - 'a']++ which can convert letter into index in array because every letter represent a number.
// If i have a letter 'a' subtracted with 'a' (a - a) then the result would be 0 (first index).
// Then we just append every combination and put them inside result as the reference point when checking or adding anagram
// This solution will give time complexity O(m * n) with m as the total words, and n as the total letter of each words. 
// There is O(26) time complexity when joining the letter count into an anagram mapping but we can ignore it since its just a constant