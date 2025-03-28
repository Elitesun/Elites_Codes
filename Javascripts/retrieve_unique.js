// the task is given very large arrays you are to return the unique value in it .. for example:
// [11,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10] should return 11 cause its only there once.

// the goal is to do this in O(n) time complexity and O(1) space complexity. for performance.

function findUniq(arr) {
    let counter = new Map();
    for(let num of arr){
      counter.set(num , (counter.get(num) || 0) + 1)
    }
    for ( let [key , value ] of counter){
      if (value === 1) return key;
    }
  }