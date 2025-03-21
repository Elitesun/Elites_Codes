str_numbers = ["1", "2", "three", "4"]
int_numbers = [int(x) for x in str_numbers if x.isdigit()]
print(int_numbers)  # Output: [1, 2, 4]



number = int("A", 16)
print(number)  # Output: 10


number = int("1010", 2)
print(number)  # Output: 10