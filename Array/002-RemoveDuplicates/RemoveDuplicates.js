var removeDuplicates = function(nums) {
    let out = 1
    for(let idx=0; idx < nums.length-1;idx++) {
        if (nums[idx] != nums[idx+1]) {
            nums[out] = nums[idx+1]
            out += 1 
        } 
    }
    return out
};
