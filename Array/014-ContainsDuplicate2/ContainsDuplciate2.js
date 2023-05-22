var containsNearbyDuplicate = function(nums, k) {
    let numMap = new Map();
    
    for (let i=0; i<nums.length; i++) {
        if (numMap.has(nums[i]) && Math.abs(numMap.get(nums[i])-i) <= k ) {
            return true
        }
        
        numMap.set(nums[i], i)
    }
    
    return false
};
