func containsNearbyDuplicate(nums []int, k int) bool {
    numMap := make(map[int]int)
    
    for idx, num := range nums {
        _, exist := numMap[num]
        if exist && math.Abs(float64(numMap[num]-idx)) <= float64(k) {
            return true
        }
        
        numMap[num] = idx
    }
    return false
}
