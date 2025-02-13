# Code Compilation

This README file contains a compilation of code snippets from the JavaScript and Python folders, along with explanations for each snippet.
You might not find everything here but the folders have it all . Feel free to contribute . i will apply your changes and update the README file .

## JavaScript Code Snippets

### 1. Checking if a String Starts with Something

```javascript
function areYouPlayingBanjo(name) {
  return (
    name +
    (name[0].toLowerCase() == "r" ? " plays" : " does not play") +
    " banjo"
  );
}

function areYouPlayingBanjo(name) {
  return name.toLowerCase().startsWith("r")
    ? name + " plays banjo"
    : name + " does not play banjo";
}

function areYouPlayingBanjo(name) {
  return name + (/^r/i.test(name) ? " plays " : " does not play ") + "banjo";
}
```

This function checks if the name starts with 'r' and returns a message indicating whether the person plays the banjo.

### 2. Checking if the Sum of an Array is Odd or Even

```javascript
function oddOrEven(array) {
  const res = array.reduce((sum, i) => sum + i, 0);
  return res % 2 == 0 ? "even" : "odd";
}

function oddOrEven(arr) {
  return arr.reduce((a, b) => a + b, 0) % 2 ? "odd" : "even";
}
```

This function calculates the sum of an array and returns whether the sum is odd or even.

### 3. Combining Two Strings and Returning the Longest Occurrence of Each Letter

```javascript
const longest = (s1, s2) => [...new Set(s1 + s2)].sort().join("");
```

This function combines two strings and returns the unique letters in sorted order.

### 4. Rock-Paper-Scissors Game

```javascript
function rps(p1, p2) {
  const beats = { rock: "scissors", scissors: "paper", paper: "rock" };
  if (beats[p1] === p2) return "Player 1 won!";
  if (beats[p2] === p1) return "Player 2 won!";
  return "Draw!";
}
```

This function implements the logic for a Rock-Paper-Scissors game.

### 5. Sum of Digits

```javascript
function sumOfDigits(num) {
  return num
    .toString()
    .split("")
    .reduce((sum, digit) => sum + parseInt(digit), 0);
}
```

This function calculates the sum of digits of a number.

## Python Code Snippets

### 1. Anagram in Array

```python
def stringAnagram(dictionary, query):
    anadict = {}
    for w in dictionary:
        sword = ''.join(sorted(w))
        if sword in anadict:
            anadict[sword].append(w)
        else:
            anadict[sword] = [w]

    array = []
    for word in query:
        sorted_word = ''.join(sorted(word))
        times = len(anadict.get(sorted_word, []))
        array.append(times)

    return array
```

This function counts how many anagrams exist in a given dictionary for each word in a query.

### 2. Checking if a String Starts with Something

```python
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
```

Similar to the JavaScript version, this function checks if the name starts with 'r'.

### 3. Replace First Occurrence of a Character and Delete Rest

```python
def replace_first_occurrence_and_delete_rest(input_string, old_char, new_char):
    index = input_string.find(old_char)
    if index != -1:
        modified_string = input_string[:index] + new_char
        modified_string += input_string[index + 1:].replace(old_char, "")
        return modified_string
    else:
        return input_string
```

This function replaces the first occurrence of a specified character in a string and deletes the rest.

### 4. Using the `enumerate` Function

```python
for index, season in enumerate(seasons):
    print(f"{season} is at index {index}")
```

This example demonstrates how to use the `enumerate` function to iterate over a list with indices.

### 5. Using the `filter` Function

```python
odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))
```

This example filters a list to include only odd numbers.

### 6. Using `itertools.product`

```python
import itertools
product = itertools.product(range(2), repeat=3)
filtered_product = [list(t) for t in product if sum(t) != 2]
```

This example computes the Cartesian product of input iterables and filters the results.

### 7. Rock-Paper-Scissors Game

```python
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
```

This function implements the logic for a Rock-Paper-Scissors game.

### 8. Finding the Second Smallest Number

```python
nlist.sort(key=lambda x: x[1])
secondmin = None
for score in nlist:
    if score[1] > minscore:
        secondmin = score[1]
        break
```

This code collects student names and scores, determines the second lowest score, and prints the names of students with that score.

### 9. Sum of Digits

```python
print(sum(int(i) for i in input())**2)
```

This example calculates the square of the sum of digits of a number.
