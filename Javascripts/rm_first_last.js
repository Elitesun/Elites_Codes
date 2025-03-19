// the idea or task is to given a string remove the first and last letter then return the string

// two simple methods using slice and substring

function removeChar(str){
    return str.substr(1 , str.length-2)
   
   };

   removeChar = str => str.slice(1,-1)

//    the slice method seems straightforward and simmple to understand