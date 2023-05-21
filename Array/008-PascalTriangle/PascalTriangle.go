if numRows == 0 {
        return [][]int{}
    }

    out := make([][]int, numRows)
    out[0] = []int{1}

    for i := 1; i < numRows; i++ {
        prevRow := out[i-1]
        row := make([]int, i+1)
        row[0] = 1
        row[i] = 1

        for j := 1; j < i; j++ {
            row[j] = prevRow[j-1] + prevRow[j]
        }

        out[i] = row
    }

    return out
}
