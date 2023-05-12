func searchInsert(nums []int, target int) int {
    for i:=0;i<len(nums);i++ {
        if nums[i] >= target {
            return i
        } else if i == len(nums)-1 {
            return i+1
        }
    }
    return 0
}
