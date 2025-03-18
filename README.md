# Code Compilation

This README contains a curated collection of code snippets from the JavaScript and Python folders, with clear explanations and use cases for each implementation.

## JavaScript Code Snippets

### 1. String Pattern Matching

```javascript
// Method 1: Using toLowerCase() and direct comparison
function areYouPlayingBanjo(name) {
  return name + (name[0].toLowerCase() === "r" ? " plays" : " does not play") + " banjo";
}

// Method 2: Using startsWith() for cleaner string matching
function areYouPlayingBanjo(name) {
  return name.toLowerCase().startsWith("r")
    ? name + " plays banjo"
    : name + " does not play banjo";
}

// Method 3: Using RegExp for pattern matching
function areYouPlayingBanjo(name) {
  return name + (/^r/i.test(name) ? " plays " : " does not play ") + "banjo";
}
```

These functions demonstrate different approaches to check if a name starts with 'r' (case-insensitive). Each method has its advantages:
- Method 1: Simple and straightforward
- Method 2: More readable and uses modern string methods
- Method 3: Flexible pattern matching using regular expressions

### 2. Array Sum Analysis

```javascript
function oddOrEven(array) {
  const sum = array.reduce((total, current) => total + current, 0);
  return sum % 2 === 0 ? "even" : "odd";
}

// Concise version using implicit return
const oddOrEven = arr => arr.reduce((a, b) => a + b, 0) % 2 ? "odd" : "even";
```

These functions calculate the sum of array elements and determine if the sum is odd or even. The first version is more readable, while the second is more concise using arrow functions.

### 3. String Manipulation

```javascript
const longest = (s1, s2) => [...new Set(s1 + s2)].sort().join("");
```

This elegant function:
1. Combines two strings
2. Converts to a Set to remove duplicates
3. Sorts the unique characters
4. Joins them back into a string

### 4. Game Logic Implementation

```javascript
function rps(p1, p2) {
  const beats = { rock: "scissors", scissors: "paper", paper: "rock" };
  if (beats[p1] === p2) return "Player 1 won!";
  if (beats[p2] === p1) return "Player 2 won!";
  return "Draw!";
}
```

A clean implementation of Rock-Paper-Scissors using an object to define winning combinations. The beats object makes the game logic easy to understand and maintain.

### 5. Number Processing

```javascript
function sumOfDigits(num) {
  return num
    .toString()
    .split("")
    .reduce((sum, digit) => sum + parseInt(digit), 0);
}
```

This function demonstrates chaining methods to:
1. Convert a number to string
2. Split into individual digits
3. Calculate the sum using reduce

## Python Code Snippets

### 1. String Pattern Analysis

```python
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

# Alternative using ternary operator
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"
```

Python implementations of the banjo player check, showing both traditional if-else and ternary operator approaches.

### 2. Anagram Detection

```python
def stringAnagram(dictionary, query):
    # Create a dictionary of sorted words
    anadict = {}
    for w in dictionary:
        sorted_word = ''.join(sorted(w))
        anadict.setdefault(sorted_word, []).append(w)

    # Count anagrams for each query
    return [len(anadict.get(''.join(sorted(word)), [])) for word in query]
```

This function efficiently finds anagrams by:
1. Sorting letters of each word as a key
2. Grouping words with the same sorted letters
3. Counting matches for each query

### 3. String Manipulation

```python
def replace_first_occurrence_and_delete_rest(input_string, old_char, new_char):
    index = input_string.find(old_char)
    if index != -1:
        return input_string[:index] + new_char + input_string[index + 1:].replace(old_char, "")
    return input_string
```

This function demonstrates string slicing and replacement in Python, handling edge cases appropriately.

### 4. Collection Processing

```python
# Enumerate example
for index, season in enumerate(seasons):
    print(f"{season} is at index {index}")

# Filter example
odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))

# Cartesian product with filtering
import itertools
product = itertools.product(range(2), repeat=3)
filtered_product = [list(t) for t in product if sum(t) != 2]
```

These examples show Python's powerful built-in functions for collection processing.

### 5. Game Implementation

```python
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
```

A clean Python implementation of Rock-Paper-Scissors using dictionary-based game logic.

### 6. Number Processing

```python
# Square of sum of digits
print(sum(int(i) for i in input())**2)

# Perfect square checker
import math
def find_next_square(sq):
    root = math.sqrt(sq)
    return (root + 1)**2 if root.is_integer() else -1
```

These examples demonstrate different approaches to number processing in Python, using built-in functions and the math module.
