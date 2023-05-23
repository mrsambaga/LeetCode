func romanToInt(s string) int {
    romanMap := map[string]int{
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
    }
    out := 0
    
    for idx, _ := range s {
        if idx < len(s)-1 && romanMap[string(s[idx+1])] > romanMap[string(s[idx])] {
            out -= romanMap[string(s[idx])]
        } else {
            out += romanMap[string(s[idx])]
        }
    }
    return out
}
