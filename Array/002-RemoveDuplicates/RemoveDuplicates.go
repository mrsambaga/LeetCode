func removeDuplicates(nums []int) int {
    out := 1

    for idx:=0; idx < len(nums)-1; idx++ {
        if nums[idx] != nums[idx+1] {
            nums[out] = nums[idx+1]
            out += 1
        }
    }
    return out
}
