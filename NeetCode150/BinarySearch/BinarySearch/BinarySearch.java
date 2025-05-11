package NeetCode150.BinarySearch.BinarySearch;

public class BinarySearch {
    public int search(int[] nums, int target) {
        int beginning = 0;
        int end = nums.length-1;

        while (beginning <= end) {
            int mid = (beginning + end) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] < target) {
                beginning = mid + 1;
                continue;
            }

            end = mid-1;
        }

        return -1;
    }
}