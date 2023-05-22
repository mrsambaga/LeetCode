var majorityElement = function(nums) {
    let num = new Map();
    
    for (let i=0; i < nums.length; i++) {
        if (num.has(nums[i])) {
            num.set(nums[i], num.get(nums[i]) + 1)
        } else {
            num.set(nums[i], 1)
        }
    }
    
    let idx = 0
    let count = 0
    
    for (let n of num.keys()) {
        if (num.get(n) > count) {
            count = num.get(n)
            idx = n
        }
    }
    
    return idx
};
