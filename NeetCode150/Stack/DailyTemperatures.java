package NeetCode150.Stack;

import java.util.Stack;

public class DailyTemperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                Integer resultIdx = stack.pop();
                result[resultIdx] = i - resultIdx;
            }

            stack.push(i);
        }

        return result;
    }
}

// For this problem we use stack data structure to store lower temperature index.
// We iterate through the temperatures array and compare the current temperature with the temperature at the index stored in the stack.
// If the current temperature is higher, we pop the index from the stack and calculate the difference between the current index and the index popped from the stack.
// We keep doing this until the stack is empty or the current temperature is lower than the temperature at the index stored in the stack.
// This problem has O(n) time complexity because we iterate through the temperatures array once, and O(n) space complexity because we use a stack to store the indices of the temperatures