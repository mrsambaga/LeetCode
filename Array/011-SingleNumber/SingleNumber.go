func singleNumber(nums []int) int {
    numMap := make(map[int]int)
    
    for i:=0; i<len(nums); i++ {
        _, exist := numMap[nums[i]]
        if exist {
            delete(numMap, nums[i])
        } else {
            numMap[nums[i]] = 1
        }
    }
    
    for key := range numMap {
        return key
    }
    
    return 0
}
