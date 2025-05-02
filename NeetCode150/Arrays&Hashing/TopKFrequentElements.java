import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numMap = new HashMap<>();
        
        for (int num : nums) {
            numMap.put(num, numMap.getOrDefault(num, 0) + 1);
        }
        
        List<Integer>[] bucket = new ArrayList[nums.length + 1];
        
        for (int i = 0; i < bucket.length; i++) {
            bucket[i] = new ArrayList<>();
        }
        
        for (int key : numMap.keySet()) {
            int frequency = numMap.get(key);
            bucket[frequency].add(key);
        }
        
        int[] result = new int[k];
        int index = k-1;
        
        for (int i=bucket.length-1; i > 0; i--) {
            for (int num : bucket[i]) {
                result[index] = num;
                index--;

                if (index < 0) {
                    return result;
                }
            }
        }
        
        return result;
    }
}
