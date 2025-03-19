
const reverseSeq = n => {
return Array.from({ length: n }, (_, i) => n - i);
};

// Example usage:
console.log(reverseSeq(5)); // [5, 4, 3, 2, 1]


//  Explanation:
// 1. **`Array.from({ length: n })`** creates an array of length `n`.
// 2. **`(_, i) => n - i`** fills the array by subtracting `i` from `n`, ensuring the sequence goes from `n` to `1`.

// there are multiple ways to write this : 

const reverseSeq1 = length => Array.from({length}, () => length--)


const reverseSeq2 = n => {
    return Array(n).fill(0).map((e, i) => n - i );
  };