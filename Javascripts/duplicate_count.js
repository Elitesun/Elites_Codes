// the task is to take a string and return the number of duplicate characters in it. for example:
// "aabbcde" should return 2 because there are 2 duplicate characters in it. a and b.

function duplicateCount(text){
  let counter = new Map();
  for (let char of text){
    counter.set(char, (counter.get(char) || 0) + 1);
  }
  let duplicates = 0;
  for (let [key, value] of counter){
    if (value > 1) duplicates++;
  }

}