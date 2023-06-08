var thirdMax = function(nums) {
    let newNums = [... new Set(nums)]
    newNums.sort((a,b) => b-a)
    
    if (newNums.length >= 3) {
        return newNums[2]
    } else {
        return newNums[0]
    }
};
