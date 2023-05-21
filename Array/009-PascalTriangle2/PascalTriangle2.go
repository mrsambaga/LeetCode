func getRow(rowIndex int) []int {
    out := make([][]int, rowIndex+1)
    out[0] = []int{1}
    
    for i:=1; i<rowIndex+1; i++ {
        prev := out[i-1]
        temp := make([]int, i+1)
        temp[0] = 1
        temp[i] = 1
        
        for l:=1; l<i; l++ {
            temp[l] = prev[l] + prev[l-1]
        } 
        
        out[i] = temp
    }
    
    return out[len(out)-1]
}
