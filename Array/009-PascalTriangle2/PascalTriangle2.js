var getRow = function(rowIndex) {
    let out = [[1]]
    
    for (let i = 1; i < rowIndex+1; i++) {
        let arr1 = out[out.length-1].slice()
        let arr2 = out[out.length-1].slice()
        
        arr1.push(0)
        arr2.unshift(0)
        
        for (let l = 0; l<arr1.length; l++) {
            arr1[l] += arr2[l]
        }
        out.push(arr1)
    }
    
    return out[out.length-1]
};
