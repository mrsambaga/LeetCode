var removeElement = function(nums, val) {
    let valIdx = 0

    for (let idx=0; idx < nums.length; idx++) {
        if (nums[idx] != val) {
            nums[valIdx] = nums[idx]
            valIdx += 1
        }
    }
    return valIdx
};
