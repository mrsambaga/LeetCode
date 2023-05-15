var merge = function(nums1, m, nums2, n) {
    for (let i = nums1.length-1; i > -1; i--) {
        if (m-1 >= 0 && n-1 >= 0) {
            if (nums1[m-1] > nums2[n-1]) {
                nums1[i] = nums1[m-1]
                m -= 1
            }
            else {
                nums1[i] = nums2[n-1]
                n -= 1
            }
        }
    }
    
    if (n >= 0) {
        nums1.splice(0,n,...nums2.slice(0,n))
    }
};
