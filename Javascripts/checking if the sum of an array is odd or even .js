function oddOrEven(array) {
   const res = array.reduce((sum , i) => sum + i , 0);
  return res % 2 == 0 ? 'even' : 'odd'
}



function oddOrEven(arr) {
  return arr.reduce((a,b)=>a+b,0) % 2 ? 'odd' : 'even';
}