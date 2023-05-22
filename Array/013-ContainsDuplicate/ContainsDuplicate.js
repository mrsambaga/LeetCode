var containsDuplicate = function(nums) {
    let numMap = new Map()
    
    for (let num of nums) {
        if (numMap.has(num)) {
            return true
        }
        
        numMap.set(num, 1)
    }
    
    return false
};
