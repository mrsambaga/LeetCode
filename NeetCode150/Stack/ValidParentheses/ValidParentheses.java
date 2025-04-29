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

// In this problem we can achieve optimal solution by using stack data structure using Deque Array.
// Basically, we can iterate throught the string and add the char to the stack if its an open parentheseses.
// If its a close parentheses, you can check with first element of the stack (lattest added). If its a matching type, remove it.
// The closing parentheses ALWAYS has to match with the latest added open parentheses. In the end, the stack will be empty which mean its a valid parentheses.
// This solution has O(n) time complexity (all the ltter in string) and O(n) space complexity (for storing open parentheses)

