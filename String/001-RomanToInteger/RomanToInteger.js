var romanToInt = function(s) {
    const romanMap = new Map([
        ["I", 1],
        ["V", 5],
        ["X", 10],
        ["L", 50],
        ["C", 100],
        ["D", 500],
        ["M", 1000]
    ]);
    let out = 0
    for (let i=0; i<s.length; i++) {
        if (i < s.length-1 && romanMap.get(s[i+1]) > romanMap.get(s[i])) {
            out -= romanMap.get(s[i])
        } else {
            out += romanMap.get(s[i])
        }
    }
    return out
};
