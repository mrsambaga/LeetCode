## Common Algorithm, Tools, & Tips in Array Problem Set

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










