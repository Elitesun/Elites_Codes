// the task is given two arrays and you need to return the array with 
// the elements that are in the first array but not in the second
// there were multiple solutions to this problem.
// i used the filter method and the includes method


function array_diff(a, b) {
    return a.filter(e => !b.includes(e));
  }

//   -------------------------------------------------------------------------

  function arrayDiff(a, b) {
    let result=[]
    for (digit of a){
      if (!b.includes(digit)) result.push(digit)
    }
    return result;
  }

// ---------------------------------------------like WTF--------------------

array_diff = require("lodash").difference;

// learnt about lodash and the difference method.
// it is a very useful library that i will use in the future.


// this final one is the best one i liked cause it is short and simple and also memory efficient .

function arrayDiff(a, b) {
    let setB = new Set(b);  // Convert array b to a Set for O(1) lookup
    let result = [];

    for (let digit of a) {
        if (!setB.has(digit)) {  // Check if digit is not in b using Set
            result.push(digit);
        }
    }

    return result;
}

console.log(arrayDiff([1, 2, 3], [2, 3]));  // Output: [1]
console.log(arrayDiff([1, 2, 3], [4, 5]));  // Output: [1, 2, 3]
console.log(arrayDiff([1, 2, 2, 3], [2]));  // Output: [1, 3]
