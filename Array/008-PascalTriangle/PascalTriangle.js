var generate = function(numRows) {
    let out = [[1]]
    
    for (let i=1; i<numRows; i++) {
        let tempArray1 = out[out.length-1].slice()
        tempArray1.push(0)
        let tempArray2 = out[out.length-1].slice()
        tempArray2.unshift(0)
        for (let l=0; l<tempArray1.length; l++) {
            tempArray1[l] += tempArray2[l]
        }
        
        out.push(tempArray1)
    }
    return out
};
