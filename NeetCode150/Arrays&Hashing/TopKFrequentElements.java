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

// For this problem we can use bucket sort algorithm where we store the count of an element (get from hashmap) inside an array (bucket).
// Bucket sort algorithm is where we store both the key (num) along with its count with refernce of the index, ex: bucket[count1] = num1, bucket[count2] = num2
// The array (bucket) will have length equals to the nums length minus 1 since the extreme case is 1 num appear n times or every num appear 1 time. So 1 to n;
// Then the final loop is to iterate backward (from the highest count/index) the bucket to get all the top k frequent num.
// This problem has O(n) time complexity because there are 4 O(n) iteration, and O(n) space complexity because there are 3 O(n) array/hashmap.
