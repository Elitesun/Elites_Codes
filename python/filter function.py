numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_odd(n):
    return n % 2 != 0

odd_numbers = list(filter(is_odd, numbers))
print(odd_numbers)
# Output: [1, 3, 5, 7, 9]




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))
print(odd_numbers)
# Output: [1, 3, 5, 7, 9]




words = ["apple", "bat", "cat", "dog", "elephant"]

short_words = list(filter(lambda word: len(word) <= 3, words))
print(short_words)
# Output: ['bat', 'cat', 'dog']





numbers = [-10, -5, 0, 5, 10]

def is_positive(n):
    return n > 0

positive_numbers = list(filter(is_positive, numbers))
print(positive_numbers)
# Output: [5, 10]





students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 72},
    {"name": "Charlie", "grade": 90},
    {"name": "David", "grade": 65}
]

passing_students = list(filter(lambda student: student["grade"] >= 70, students))
print(passing_students)
# Output: [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 72}, {'name': 'Charlie', 'grade': 90}]




values = [0, 1, False, 2, '', 3, None, 4, 'Hello', 5]

filtered_values = list(filter(None, values))
print(filtered_values)
# Output: [1, 2, 3, 4, 'Hello', 5]



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter(lambda n: n % 2 != 0, numbers)
odd_numbers_list = [n for n in odd_numbers]
print(odd_numbers_list)
# Output: [1, 3, 5, 7, 9]