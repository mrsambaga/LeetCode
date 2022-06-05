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






