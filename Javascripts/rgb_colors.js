// the task is to find the hex value of the closest color to the given rgb value
// negative values are rounded to 0
// values greater than 255 are rounded to 255

function rgb(r, g, b) {
    let g1 = Math.min(255 , Math.max(0 , g))
    let b1 = Math.min(255 , Math.max(0 , b))
    let r1 = Math.min(255 , Math.max(0 , r))
    return [r1 , g1 , b1].map(num => num.toString(16).padStart(2 , "0")).join("").toUpperCase()
    
  }

// i came up with this solution on my own. it could be easier if the the rgb were all positive but ahhh

// a better solution

function rgb(r, g, b) {
    return [r, g, b].map(function(x) {
      return ('0' + Math.max(0, Math.min(255, x)).toString(16)).slice(-2)
    }).join('').toUpperCase()
  }
// or
  function rgb(r, g, b) {
    return [r, g, b]
      .map(num => Math.min(255, Math.max(0, num)) // Clamp between 0 and 255
      .toString(16).padStart(2, "0")) // Convert to hex with padding
      .join("").toUpperCase();
  }
//   this are the same but optimized