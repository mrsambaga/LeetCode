class Solution {
    public boolean isAnagram(String s, String t) {
       HashMap<Character, Integer> letterMap = new HashMap<>();

        for (char c : s.toCharArray()) {
            charFreq.put(c, charFreq.getOrDefault(c, 0) + 1);
        }

        for (char letter : t.toCharArray()) {
            if (!charFreq.containsKey(c) || charFreq.get(c) == 0) {
                return false;
            }

            charFreq.put(c, charFreq.get(c) - 1);
        }

        return true;
    }
}

//This solution has O(n+m) time complexity (2 for loop) with O(k) space complexity (for storing unique letter in a hash map)
