// you are given an array whith numbers and strings . your work is to give bak the sum . of each element including the string like "123"

function sumMix(x){
    let result = 0;
    for (let n of x) {
      result += parseInt(n);
    }
    return result;
  }


//   diabolical 

function sumMix(x){
    return eval( x.join("+") )
  }