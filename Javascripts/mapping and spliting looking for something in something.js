function fakeBin(x){
  return x.split("").map(i => (i < 5 ? '0' : '1')).join("");
}