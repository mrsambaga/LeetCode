package LongestConsecutiveSequence;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collector;
import java.util.stream.Collectors;

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

public class LongestConsecutiveSequenceOptimal {
    public int longestConsecutive(int[] nums) {
        if (nums.length <= 1) {
            return nums.length;
        }

        Set<Integer> numSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int maximumConsecutive = 0;

        for (Integer num : numSet) {
            if (!numSet.contains(num-1)) {
                int currentConsecutive = 1;
                while (numSet.contains(num+currentConsecutive)) {
                    currentConsecutive += 1;
                }

                maximumConsecutive = Math.max(maximumConsecutive, currentConsecutive);
            }
        }

        return maximumConsecutive;
    }
}

// This is the optimal solution for the problem.
// We have to find the beginning of the seqeuence by checking if n-1 exist in set.
// If it doesnt, that mean it is the beginning of sequence and we can check if n+1 exist and repeat it to count the consecutive number;
// This solution has O(n) time complexity beause every element is checked once (in for lopp or in while loop) and O(n) space complexity for storing set.
