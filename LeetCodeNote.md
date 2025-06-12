## Common Algorithm, Data Structures, Tools, & Tips

## Hash Map

Hash map algorithm works by storing the data in a dictionary during an interation and check if a condition is met everytime it gets updated by new data from iteration.
If the condition is met, we can access information that is stored in the dictionary.
Example (two sum problem) :

```
num_map = {}
for i, num in enumerate(nums):
  remainder = target - nums[i]
  if remainder in num_map:
    return i,num_map[remainder]
  num_map[num] = i
```

In this code, a dictionary is used to store a number and its index. We find if a certain number is in the dictionary every iteration, then return the value which is an index if its true.

## Binary Search

Binary search is a search algorithm that is used to cut down iteration time by dividing the search area by 2.
Example (Search Insert Position) :

```
low, high = 0, len(nums)
while low<high :
  mid = (low+high)//2
  if nums[mid] == target:
    return mid
  elif nums[mid] < target:
    low = mid + 1
  else:
    high = mid
return low
```

In this code, we are searching a certain number in the list. Since the list is ordered, we can easily determine if the target is in the first half or second half.
Then, we can remove the other half and repeat the process until we find the target. This will significantly reduce the time than doing basic iteration.

## Kadane Algorithm

Kadane algorithm is an algorithm to find the maximum value of sum of subarray .
Example (maximum subarray) :

```
class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
```

Kadane algorithm works by keeping all the value of sum of subarray in every element up to that point by adding the previous element to the current element
and repeat it in an iteration for all element. If we do this in an iteration, we will have the sum of subarray up to that point, ex : [1,2,3] -> [1,3,6].
But there's is catch, we want to find the maximum value of subarray. So, the Kadane algorithm will perform the addition (previous element + current element) if the previous element is positive (that mean the cumulative is also positive too). This is because the negative value will not help making the maximum subarray.
If we encounter a negative value, we break and go to the next value (meaning we move to another subarray).

## Stacks

Stacks is a linear data structures consist of 2 operation which is push and pop on the top element. It is used to make undo mechanism or checking valid parentheses pair.
Example (valid parentheses) :

```
class Solution(object):
    def isValid(self, s):
        stacks = []
        for x in s:
            if x == "{":
                stacks.append('}')
            elif x == "[":
                stacks.append(']')
            elif x == '(':
                stacks.append(')')
            elif len(stacks)>0 and x == stacks[-1]:
                stacks.pop()
            else :
                return False
        return stacks == []
```

Stacks works by pushing the respective close parentheses to the list everytime we encounter open parentheses. Then, if we encounter close parentheses, check if its the same with the top element. If it is, pop that element. If not, that mean its not valid parentheses. In the end, check if the stacks are empty to make sure there are no open parentheses that are not closed.

## Bucket Sort Algorithm

Bucket Sort is a comparison sorting algorithm that operates by dividing elements from an array into a finite number of "buckets." Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sort algorithm. It is particularly effective when the input data is uniformly distributed over a range.

Example : TopKFrequentElement

```
List<Integer>[] bucket = new ArrayList[nums.length + 1];

//Create bucket        
for (int i = 0; i < bucket.length; i++) {
  bucket[i] = new ArrayList<>();
}

//Put map key (number) to bucket with value (frequency) as index        
for (int key : numMap.keySet()) {
    int frequency = numMap.get(key);
    bucket[frequency].add(key);
}
        
int[] result = new int[k];
int index = k-1;

//Iterate bucket array backwards (meaning you get the top k most frequent element)
for (int i=bucket.length-1; i > 0; i--) {
    for (int num : bucket[i]) {
        result[index] = num;
        index--;

        if (index < 0) {
            return result;
        }
    }
}
```

This algorithm works by putting number as key to the bucket and frequency as the array index. This works because the number can appear
maximum in an array is N times where N is the length of array. After that, the array index represent the frequency of the number appear in the array.
That mean, we can just iterate from the back to get the highest index of array (highest frequency).
This algorithm has O(n) time complexity on average but can also have O(n^2) on worst case where every number appear 1 time (1 bucket has N elements).
