# Define a list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Define a list of items to filter
filter_list = ['apple', 'date', 'elderberry']

# Use fromlist to get a new list containing only the items from my_list that are also in filter_list
new_list = [item for item in my_list if item in filter_list]

print(new_list)
['apple', 'date', 'elderberry']
