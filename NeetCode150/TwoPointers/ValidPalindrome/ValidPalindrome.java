package NeetCode150.TwoPointers.ValidPalindrome;

public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        StringBuilder cleanedString = new StringBuilder();
        for (Character str : s.toCharArray()) {
            if (Character.isLetterOrDigit(str)) {
                cleanedString.append(Character.toLowerCase(str));
            }
        }

        StringBuilder reverseString = new StringBuilder();
        for (int i=s.length()-1; i>=0; i--) {
            if (Character.isLetterOrDigit(s.charAt(i))) {
                reverseString.append(Character.toLowerCase(s.charAt(i)));
            }
        }

        return reverseString.toString().equals(cleanedString.toString());
    }
}

// The first solution we can use is to do iteration twice. First we can clean the original string from non alphanumeric
// Then we reverse the string. Finally, we compare both string.
// This solution is O(n) time complexity (2 linear looping) and O(n) space complexity (for storing string)


