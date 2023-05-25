var summaryRanges = function(nums) {
    let res = []
    
    for (let i=0; i<nums.length; i++) {
        if (res.length && res[res.length-1][1] === nums[i] - 1) {
            res[res.length-1][1] = nums[i]
        } else {
            res.push([nums[i],nums[i]])
        }
    }
    
    let out = []
    
    for (let i=0; i<res.length; i++) {
        if (res[i][0] != res[i][1]) {
            out.push(`${res[i][0]}->${res[i][1]}`)
        } else {
            out.push(String(res[i][0]))
        }
    }
    
    return out
};
