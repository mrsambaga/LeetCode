import java.util.ArrayList;
import java.util.List;

public class EncodeAndDecodeString {
    public String encode(List<String> strs) {
        StringBuilder strings = new StringBuilder();
        strs.stream().forEach((str) -> 
            strings.append(str).append('|')
        );
        
        return strings.toString();
    }

    public List<String> decode(String str) {
        StringBuilder tempString = new StringBuilder();
        List<String> outputString = new ArrayList<>();
        for (String letter : str.split("")) {
            if (letter.equals("|")) {
                outputString.add(tempString.toString());
                tempString = new StringBuilder();
                continue;
            }

            tempString.append(letter);
        }

        return outputString;
    }
}

// The simplest solution for this is to add non ascii character between the word as a "marker"
// Then during iteration, we just need to check those marker to differentiate between words
// This solution has O(n) time complixity for each method (decode & encode) and O(m+n) space complexity
// Where m is the total number of words & n is the total number of character.
