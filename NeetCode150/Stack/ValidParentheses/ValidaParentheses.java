package NeetCode150.Stack.ValidParentheses;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<Character>();

        Map<Character, Character> parentheses = Map.of(
            '(', ')',
            '{', '}',
            '[', ']'
        );

        for (char letter : s.toCharArray()) {
            if (parentheses.containsKey(letter)) {
                stack.push(letter);
                continue;
            }

            if (stack.isEmpty() || !parentheses.get(stack.getFirst()).equals(letter)) {
                return false;
            }

            stack.pop();
        }

        return stack.isEmpty();
    }
}

