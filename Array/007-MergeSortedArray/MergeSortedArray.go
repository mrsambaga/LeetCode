func merge(nums1 []int, m int, nums2 []int, n int)  {
    
    for i:=len(nums1)-1; i>=0; i-- {
        if m > 0 && n > 0 {
            if nums1[m-1] > nums2[n-1] {
                nums1[i] = nums1[m-1]
                m -= 1
                
            } else {
                nums1[i] = nums2[n-1]
                n -= 1
            }
        }
    } 
    
    if n >= 0 {
        copy(nums1[:n], nums2[:n])
    }
        
}
