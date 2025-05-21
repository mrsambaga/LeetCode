package NeetCode150.Stack.MinStack;

import java.util.Stack;

public class MinStack {
    Stack<Integer> stack = new Stack<>();
    Stack<Integer> minStack = new Stack<>();

    public MinStack() {
        
    }
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        if (stack.pop().equals(minStack.peek())) {
            minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

// For this solution we are using two stacks.
// The first stack is the main stack that we are pushing and popping from.
// The second stack is the minStack so store the minimum values.
// We are pushing the values from the main stack to the minStack if the value is less than or equal to the current min value.
// When we pop from the main stack, we also pop from the minStack if the value is the same as the top of the minStack.
// This solution is O(1) time complexity for all operations.


