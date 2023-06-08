// Clear & straightforward solution

var intersection = function(nums1, nums2) {
    let out = []
    for (let i=0; i<nums1.length; i++) {
        if (nums2.includes(nums1[i])) {
           out.push(nums1[i])
        }
    }
    
   let setOut = Array.from(new Set(out))
   return setOut
};

// Simplest solution

var intersection = function(nums1, nums2) {
    return [...new Set(nums1)].filter(num => nums2.includes(num));
};


