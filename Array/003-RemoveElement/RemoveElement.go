func removeElement(nums []int, val int) int {
    valIdx := 0
    for i:=0; i < len(nums); i++ {
        if nums[i] != val {
            nums[valIdx] = nums[i]
            valIdx += 1
        }
    }
    return valIdx
}
