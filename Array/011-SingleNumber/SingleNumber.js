var singleNumber = function(nums) {
    let numMap = new Map()
    
    for (let i=0; i<nums.length; i++) {
        if (numMap.has(nums[i])) {
            numMap.delete(nums[i])
        } else {
            numMap.set(nums[i], 1)
        }
    }
    
    const keys = [...numMap.keys()]
    return keys[0]
};
