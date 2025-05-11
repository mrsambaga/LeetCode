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

// The first solution we can use is to do iteration twice. First we can clean the original string from non alphanumeric
// Then we reverse the string. Finally, we compare both string.
// This solution is O(n) time complexity (2 linear looping) and O(n) space complexity (for storing string)


    public boolean isPalindromeOptimal(String s) {
        int frontPointer = 0;
        int backPointer = s.length()-1;

        while (frontPointer < backPointer) {
            while (frontPointer < backPointer && !Character.isLetterOrDigit(s.charAt(frontPointer))) {
                frontPointer++;
            }

            while (frontPointer < backPointer && !Character.isLetterOrDigit(s.charAt(backPointer))) {
                backPointer--;
            }

            if (Character.toLowerCase(s.charAt(frontPointer)) != Character.toLowerCase(s.charAt(backPointer))) {
                return false;
            }

            frontPointer++;
            backPointer--;
        }

        return true;
    }

// Another better solution we can use is to use two pointer. We can start frontPointer from index 0 and back pointer from last index
// Then we move until both meet or pass each other. We ofcourse check if the letter is alphanum.
// If not, then we move to the next until we meet an alphanum. Then we compare them. If its not the same, that mean string are not palindrome.
// This solution has O(n) time complexity (we iterate all letter once) and O(1) space complexity because we store only 1 thing (index number)
}

