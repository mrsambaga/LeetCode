// Brute force way 

func twoSum(nums []int, target int) []int {
    for idx1, num1 := range nums {
        for idx2, num2 := range nums {
            if (num1+num2 == target) && (idx1 != idx2) {
                return []int{idx1,idx2}
            }
        }
    }
    return []int{}
}

// Optimal way (using hash map)

func twoSum(nums []int, target int) []int {
    hashMap := make(map[int]int)

    for idx, num := range nums {
        remainder := target - num
        idx2, ok := hashMap[remainder]
        if ok {
            return []int{idx2, idx}
        }
        hashMap[num] = idx
    }

    return []int{}
}
