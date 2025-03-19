// take a string(name) and return the first two letters of the string

function abbrevName(name){
    return name.split(" ").map(word => word[0].toUpperCase()).join("."); 
   
}

// another similar way :
function abbrevName(name){

    var nameArray = name.split(" ");
    return (nameArray[0][0] + "." + nameArray[1][0]).toUpperCase();
  }