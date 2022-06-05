## Common Algorithm, Tools, & Tips in Array Problem Set

## Hash Map
Hash map is usually used to store data in a dictionary during an interation and check if a condition is met everytime it gets updated by new data from iteration.

`Example (two sum problem) :
num_map = {}
for i, num in enumerate(nums):
  remainder = target - nums[i]
  if remainder in num_map:
    return i,num_map[remainder]
  num_map[num] = i`

In this code, a dictionary is used to store a number and its index. We find if a certain number is in the dictionary every iteration, then return the value which is an index if its true.




