# just found a lib called statistics that has a function called mean that returns the average of a list
# so I can just use that function

from statistics import mean
def find_average(numbers):
    if len(numbers) < 1 : return 0
    return mean(numbers)

# so instead of summing the list and dividing by the length of the list, I can just use the mean function
# and it will return the average of the list