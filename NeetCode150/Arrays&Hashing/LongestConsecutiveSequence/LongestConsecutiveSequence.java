package LongestConsecutiveSequence;

import java.util.Arrays;

public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        if (nums.length <= 1) {
            return nums.length;
        }

        int maximumConsecutive = 0;
        int currentConsecutive = 1;
        Arrays.sort(nums);

        for (int i=1; i<nums.length; i++) {
            if (nums[i] == nums[i-1]) {
                continue;
            }
            if (nums[i] == nums[i-1] + 1) {
                currentConsecutive += 1;
                continue;
            }

            maximumConsecutive = Math.max(maximumConsecutive, currentConsecutive);
            currentConsecutive = 1;
        }

        return Math.max(maximumConsecutive, currentConsecutive);
    }
}

// In this problem the easiest way to solve is just to use sort. We can sort the array and iterate them to find the max consecutive.
// This solution, however is not the optimal solution because it has O(n log n) time complexity and O(1) space complexity
// This is because the sorting algorithm take about O(n log n) time complexity.
