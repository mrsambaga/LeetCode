func plusOne(digits []int) []int {
    carry := 0
    digits[len(digits)-1] += 1
    if digits[len(digits)-1] > 9 {
        digits[len(digits)-1] = 0
        carry = 1
    }
    
    for i:=len(digits)-1; i>-1 ; i-- {
        if (digits[i] + carry > 9) {
            digits[i] = 0
            carry = 1
        } else {
            digits[i] += carry
            carry = 0
        }
    }
    
    if carry > 0 {
        digits[0] = 1
        digits = append(digits, 0)
    }
    
    return digits
}
