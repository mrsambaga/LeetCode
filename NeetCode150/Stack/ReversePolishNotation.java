package NeetCode150.Stack;

import java.util.Stack;

public class ReversePolishNotation {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {
            switch (token) {
                case "+":
                    stack.push(stack.pop() + stack.pop());
                    break;
                case "-":
                    int first = stack.pop();
                    int second = stack.pop();
                    stack.push(second - first);
                    break;
                case "*":
                    stack.push(stack.pop() * stack.pop());
                    break;
                case "/":
                    int divisor = stack.pop();
                    int dividend = stack.pop();
                    stack.push(dividend / divisor);
                    break;
                default:
                    stack.push(Integer.parseInt(token));
                    break;
            }
        }

        return stack.pop();
    }
}

// For this problem, we can use a stack to store the numbers.
// When we encounter a number, we just push it onto the stack.
// When we encounter an operand, we pop the last two numbers from the stack and perform the operation.
// We then push the result back onto the stack.
// At the end, we return the last number in the stack as the result.
// This solution is O(n) time complexity for iterating through the tokens and O(n) space complexity for the stack.


