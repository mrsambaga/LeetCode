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
