func containsDuplicate(nums []int) bool {
    numMap := make(map[int]int)
    
    for i:=0; i<len(nums); i++ {
        _, exist := numMap[nums[i]]
        if exist {
            return true
        }
        
        numMap[nums[i]] = 1
        
    }
    return false
}
