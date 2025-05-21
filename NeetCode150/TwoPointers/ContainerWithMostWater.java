package NeetCode150.TwoPointers;

public class ContainerWithMostWater {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxArea = 0;

        while (left < right) {
            int area = Math.min(heights[left], heights[right]) * (right - left);

            if (area > maxArea) {
                maxArea = area;
            }

            if (heights[left] < heights[right]) {
                left += 1;
                continue;
            }
            

        }

        return maxArea;
    }
}

// For this problem we could use double pointer approach
// We set left and right pointer and calculate the area
// We shift the smaller pointer since its impossible to achieve bigger area if we shifted the bigger pointer
// Keep shifting until both pointer meet each other
// This solution has O(n) time complexity and O(1) space complexity
