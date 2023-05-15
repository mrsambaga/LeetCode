var plusOne = function(digits) {
    let carry = 0
    digits[digits.length-1] += 1
    if (digits[digits.length-1] > 9) {
        digits[digits.length-1] = 0
        carry = 1
    }

    for (let i=digits.length-2; i > -1; i--) {
        if (digits[i] + carry > 9) {
            digits[i] = 0
            carry = 1
        } else {
            digits[i] += carry
            carry = 0
        }  
    }

    if (carry > 0) {
        digits[0] = 1
        digits.push(0)
    }
    
    return digits
};
