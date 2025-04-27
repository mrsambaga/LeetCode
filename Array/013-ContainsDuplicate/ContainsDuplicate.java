class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> checkedValue = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (checkedValue.contains(nums[i])) {
                return true;
            }

            checkedValue.add(nums[i]);
        }

        return false;
    }
}

//Use set for efficient memory (compared to hash map) and faster search (compared to list or array)
