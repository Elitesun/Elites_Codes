# A bruh number of n is square of sum digits of n
# Example
# Input
# 11
# Output
# 4
print(sum(int(i) for i in input())**2)



s = input()
total_sum = sum(x * 2 if x % 2 == 0 else x for x in (ord(i) for i in s))
print(total_sum)