numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x * x, numbers)
print(list(squared_numbers))
# Output: [1, 4, 9, 16, 25]



numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed_numbers = map(lambda x, y: x + y, numbers1, numbers2)
print(list(summed_numbers))
# Output: [5, 7, 9]



numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed_numbers = map(lambda x, y: x + y, numbers1, numbers2)
print(list(summed_numbers))
# Output: [5, 7, 9]



str_numbers = ["1", "2", "3"]
int_numbers = map(int, str_numbers)
print(list(int_numbers))
# Output: [1, 2, 3]



words = ["hello", "world"]
upper_words = map(str.upper, words)
print(list(upper_words))
# Output: ['HELLO', 'WORLD']



from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x * x, numbers)
sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)
print(sum_of_squares)
# Output: 55