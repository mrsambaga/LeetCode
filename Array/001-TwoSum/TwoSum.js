//Brute force way (Javascript) :

var twoSum = function(nums, target) {
    for (let idx1 = 0; idx1 < nums.length; idx1++) {
        for (let idx2 = idx1+1; idx2 < nums.length; idx2++) {
            if (nums[idx1] + nums[idx2] == target) {
                return [idx1,idx2]
            }
        }
    }
};

//Optimal way using hasmap (Javascript) :

var twoSum = function(nums, target) {
    const numMap = new Map()

    for (idx = 0; idx < nums.length; idx++) {
        const remainder = target - nums[idx]
        if (numMap.has(remainder)) {
            return [numMap.get(remainder), idx]
        }
        numMap.set(nums[idx], idx)
    }
};
