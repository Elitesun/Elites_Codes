import itertools

# Compute the cartesian product
product = itertools.product(range(2), repeat=3)

# Filter the list and remove any list in which the sum of the elements is equal to 2
filtered_product = [list(t) for t in product if sum(t) != 2]

# Print the result
print(filtered_product)

#normally it returns tuples.
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]






You can simplify and shorten the code while keeping the functionality intact. Here's a more concise version:

```python
import itertools

x, y, z, n = (int(input()) for _ in range(4))

result = [list(t) for t in itertools.product(range(x+1), range(y+1), range(z+1)) if sum(t) != n]
print(result)
```

### Explanation:
1. **Input Handling**: The input values for `x`, `y`, `z`, and `n` are gathered using a single line with a generator.
2. **Product and Filtering**: The `itertools.product` function generates all possible combinations of the ranges `[0, x]`, `[0, y]`, and `[0, z]`. The list comprehension filters out combinations where the sum equals `n`.
3. **Result**: The resulting list of lists is printed.

### Example:
If `x = 1`, `y = 1`, `z = 1`, and `n = 2`, the output will be:

```python
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```