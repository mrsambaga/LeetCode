func intersection(nums1 []int, nums2 []int) []int {
    var numMap = map[int]bool{}
    var numArr = []int{}
    
    for _,num := range nums1 {
        numMap[num] = true
    }
    
    for _,num := range nums2 {
        if numMap[num] == true {
            numArr = append(numArr, num)
            numMap[num] = false
        }
    }
    
    return numArr
}
